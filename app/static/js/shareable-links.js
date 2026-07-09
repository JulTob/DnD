(function() {
                function canonicalPath(pathname) {
                    var path = pathname || '/';
                    var marker = '/character/';
                    var idx = path.indexOf(marker);
                    if (idx >= 0) {
                        path = path.slice(0, idx + 1);
                    } else if (path.endsWith('/character')) {
                        path = path.slice(0, -'character'.length);
                    }
                    return path || '/';
                }

                function installHandler() {
                    if (typeof Shiny === 'undefined' || !Shiny.addCustomMessageHandler) return false;
                    if (window.__characterUrlHandlerInstalled) return true;
                    window.__characterUrlHandlerInstalled = true;

                    function setShareStatus(text, isError) {
                        var statusNode = document.getElementById('share-copy-status');
                        if (!statusNode) return;
                        statusNode.textContent = text || '';
                        statusNode.style.color = isError ? '#aa0a12' : '';
                        if (window.__shareStatusTimer) {
                            clearTimeout(window.__shareStatusTimer);
                        }
                        if (text) {
                            window.__shareStatusTimer = setTimeout(function() {
                                if (statusNode.textContent === text) {
                                    statusNode.textContent = '';
                                }
                            }, 2600);
                        }
                    }

                    function copyText(text) {
                        if (navigator.clipboard && navigator.clipboard.writeText) {
                            return navigator.clipboard.writeText(text);
                        }
                        return new Promise(function(resolve, reject) {
                            try {
                                var ta = document.createElement('textarea');
                                ta.value = text;
                                ta.style.position = 'fixed';
                                ta.style.left = '-9999px';
                                document.body.appendChild(ta);
                                ta.focus();
                                ta.select();
                                var ok = document.execCommand('copy');
                                document.body.removeChild(ta);
                                if (!ok) throw new Error('execCommand copy failed');
                                resolve();
                            } catch (err) {
                                reject(err);
                            }
                        });
                    }

                    function normalizeShareHash(rawValue) {
                        if (rawValue == null) return '';
                        var value = String(rawValue).trim();
                        if (!value) return '';
                        if (/^[a-z]+:\/\//i.test(value)) {
                            try {
                                value = new URL(value).hash || '';
                            } catch (_) {
                                return '';
                            }
                        }
                        if (value.startsWith('#')) value = value.slice(1);
                        if (!value) return '';
                        if (value[0] !== '/') {
                            try {
                                var decoded = decodeURIComponent(value);
                                if (decoded && decoded !== value) value = decoded;
                            } catch (_) {
                                // keep original
                            }
                        }
                        value = value.replace(/^\/+/, '');
                        if (value.toLowerCase().startsWith('character/')) {
                            value = value.slice('character/'.length);
                        }
                        var parts = value.split('/').filter(Boolean);
                        if (parts.length < 6) return '';
                        return '#/' + parts.slice(0, 6).join('/');
                    }

                    function extractHashFromPath(pathname) {
                        var path = pathname || '';
                        var marker = '/character/';
                        var idx = path.indexOf(marker);
                        if (idx < 0) return '';
                        return '#/' + path.slice(idx + marker.length).replace(/^\/+/, '');
                    }

                    function hashFromQuery(search) {
                        try {
                            var params = new URLSearchParams(search || '');
                            var seed = params.get('seed');
                            if (!seed) return '';
                            var level = params.get('level') || '1';
                            var species = params.get('species') || 'random';
                            var background = params.get('background') || 'random';
                            var charClass = params.get('char_class') || 'random';
                            var gender = params.get('gender') || 'random';
                            return '#/' + [
                                encodeURIComponent(level),
                                encodeURIComponent(species),
                                encodeURIComponent(background),
                                encodeURIComponent(charClass),
                                encodeURIComponent(gender),
                                encodeURIComponent(seed)
                            ].join('/');
                        } catch (_) {
                            return '';
                        }
                    }

                    function buildShareUrl() {
                        var hash = normalizeShareHash(window.location.hash || '');
                        if (!hash && window.__characterShareHash) {
                            hash = normalizeShareHash(window.__characterShareHash);
                        }
                        if (!hash) {
                            hash = normalizeShareHash(extractHashFromPath(window.location.pathname));
                        }
                        if (!hash) {
                            hash = normalizeShareHash(hashFromQuery(window.location.search));
                        }
                        if (!hash) return '';
                        var basePath = canonicalPath(window.location.pathname);
                        var origin = window.location.origin || '';
                        return (origin ? origin : '') + basePath + hash;
                    }

                    function fallbackCopyPrompt(url) {
                        try {
                            window.prompt('Copy this link:', url);
                        } catch (_) {
                            // ignore
                        }
                    }

                    Shiny.addCustomMessageHandler('update_character_url', function(msg) {
                        if (!msg) return;
                        var base = canonicalPath(window.location.pathname);
                        var currentHash = window.location.hash || '';
                        var nextUrl = null;
                        if (typeof msg.hash === 'string' && msg.hash.length > 0) {
                            var nextHash = normalizeShareHash(msg.hash) || (msg.hash.startsWith('#') ? msg.hash : ('#' + msg.hash));
                            window.__characterShareHash = nextHash;
                            nextUrl = base + nextHash;
                        } else if (typeof msg.path === 'string' && msg.path.length > 0) {
                            var pathSuffix = msg.path.replace(/^\/+/, '');
                            nextUrl = base + pathSuffix + currentHash;
                        } else if (typeof msg.query === 'string') {
                            nextUrl = base + msg.query + currentHash;
                        }
                        if (!nextUrl) return;
                        if (window.history && window.history.replaceState) {
                            window.history.replaceState(null, '', nextUrl);
                        } else {
                            window.location.href = nextUrl;
                        }
                    });

                    Shiny.addCustomMessageHandler('set_share_hash', function(msg) {
                        var incoming = msg && typeof msg.hash === 'string' ? msg.hash : '';
                        var normalized = normalizeShareHash(incoming);
                        if (normalized) {
                            window.__characterShareHash = normalized;
                        }
                    });

                    document.addEventListener('click', function(ev) {
                        var target = ev.target;
                        var btn = target && target.closest ? target.closest('#btn_copy_char_link') : null;
                        if (!btn) return;
                        var shareUrl = buildShareUrl();
                        if (!shareUrl) {
                            setShareStatus('Generate a character first.', true);
                            return;
                        }
                        copyText(shareUrl).then(function() {
                            setShareStatus('Link copied.', false);
                        }).catch(function() {
                            setShareStatus('Clipboard blocked. Copy from dialog.', true);
                            fallbackCopyPrompt(shareUrl);
                        });
                    });
                    return true;
                }

                if (!installHandler()) {
                    var tries = 0;
                    var maxTries = 80;
                    var timer = setInterval(function() {
                        tries += 1;
                        if (installHandler() || tries >= maxTries) {
                            clearInterval(timer);
                        }
                    }, 100);
                    window.addEventListener('shiny:connected', installHandler, { once: true });
                }
            })();
