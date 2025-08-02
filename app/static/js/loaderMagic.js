/* MagicLoader.js  ✨
 * Animación de círculo mágico + control del loader
 * Autor: ChatGPT (o3)
 */

// ----  GLOBALS  -------------------------------------------------
const TAU = Math.PI * 2;

let solBaseScale = 0.18;
let solBeatAmp   = 0.10;   // 8 % size pulsation
let solSpinSpeed = 0.0;    // degrees per frame   (tweak to taste)

let backgroundAlpha = 0;  // Start fully transparent
const maxAlpha = 255;

let polygons = [];          // will hold every planet/poly
const MIN_SIDES = 3;
const MAX_SIDES = 12;

const angleCache = {};

function getAngles(sides) {
		if (!angleCache[sides]) {
				angleCache[sides] = Array.from({length: sides},
				(_, i) => (TAU * i) / sides);
				}
		return angleCache[sides];
		}

/* --------------------  1. POOLS DE SÍMBOLOS  -------------------- */
const spinnerChars = [
  '⌭','⧲','※','⚕','☥',
  '☢','☘','𓂀','᯼','۞','࿄','✡','⍟','⭒','✩','✯','⛤','⛧','⛥',
  '⛦','⚝','⭑','☆','✧','❉','❄','❅','❆',
  '☬','☫','۝','۩','؎','⧝','𖧵','𓇬','🜹','𖣊','𖥠','🝞','🝟',
  '⏣','⬠','⬡','Ψ','ℜ','⳩','Ω','Ω','℧','𐃢','𐃯','♧','♡','♢','♤',
  '𓄀','𓆗','𓆙','𓆚','𐦐','࿓','࿔','༄','༅','༆','༻','༺',
  '⛩','♨','𐂡','𐁊','𐀼','⚕︎','⛻','🝤','🝪','🜾','🝁','🜱','𝛀','Ʊ',
  '⏲','⚳','⚴','⚵','⚶','⚸','♆','♅','♄','♃','♁','☿','🜯','🜩','🜦',
  '🜥','🜣','⛢','𓍢','𝖋','☉','✝︎','✠','☩','♰','♱','☓','⚜︎',
  '❀','✿','❦','⏚','Θ','ϟ',
  'ᚠ','ᚡ','ᚣ','ᛃ','ᛄ','ᛆ','ᛈ','ᛉ','ᛕ','ᛖ','ᛗ','ᛘ','ᛙ','ᛪ',
  'ᛩ','ᛨ','ᛦ','ᛥ','ᛤ','ᛣ','ᛢ','ᛡ','ᛟ','ᛞ','ᛝ','ᛜ','ᛰ',
  'ᛯ','ᛮ','᛭','᛬','᛫','⚊','⚋','⚌','⚍','⚎','⚏','𝌀','𝌁','𝌂',
  '𝌃','𝌄','𝌅','☰','☱','☲','☳','☴','☵','☶','☷',
  'ༀ','༁','༂','༃','༄','༅','༆','༇','༊','༒','༓','༔','༗','◇','◈',
  '✦','○','☉', '⛧','✶','⭒','✩','✯','⛤','⛧','⛥',
	'⛦','⚝','♁','★', 'ᚠ','ᚡ','ᚢ','ᚣ','ᚤ','ᚥ',
	'ᚦ','ᚧ','ᚨ','ᚩ','ᚪ','ᚵ','ᚴ','ᚳ','ᚲ','ᚱ',
	'ᚰ','ᚯ','ᚮ','ᚭ','ᚬ','ᚫ','ᚶ','ᚷ','ᚸ','ᚹ','ᚺ',
	'ᚻ','ᚼ','ᚽ','ᚾ','ᚿ','ᛀ','ᛋ','ᛊ','ᛉ','ᛈ',
	'ᛇ','ᛆ','ᛅ','ᛄ','ᛃ','ᛂ','ᛁ','ᛌ','ᛍ','ᛎ',
	'ᛏ','ᛐ','ᛑ','ᛒ','ᛓ','ᛔ','ᛕ','ᛖ','ᛡ','ᛠ','ᛟ',
	'ᛞ','ᛝ','ᛜ','ᛛ','ᛚ','ᛙ','ᛘ','ᛗ','ᛢ',
	'ᛣ','ᛤ','ᛥ','ᛦ','ᛧ','ᛨ','ᛩ','ᛪ','᛫','᛬',
	'᛭','ᛮ','ᛯ','ᛰ',
];
const centerPool = [
	'☯', '🜁','⌭','⧲','♔','♕','♖','♗', '𖣓','֎','֍','𖣐','⌘',
	'♙','⚚','☤','※','⚕','☥', '♔','♕','♖','♗','♙','⚚','☤',
	'🜏','☠','☣','⚖','⚛','⎈','☸','𑁍','⚙︎','☯','࿊','࿋','࿌',
	'🜁', '𓌖', '🜏','☠','☣','⚖','⚛','⎈','☸','𑁍','⚙︎',
	'☯','࿊','࿋','࿌','☮',"◯",'⎊','⏁','⏄','⏀','⏃','⏂','⏅',
	];
const orbitPool  = spinnerChars;

/* --------------------  2. P5 SKETCH  -------------------- */
let centerSymbol, orbitSymbols = [];

/* Refresca símbolos cada vez que volvemos a mostrar el loader */
function initSymbols () {
	centerSymbol = random(centerPool);
	orbitSymbols = Array.from({ length: int(random(4, 9)) }, () => {
		const count = int(random(1, 4)); // 1–3 children
		const baseSpeed = random([-1, 1]) * random(0.5, 2.0); // mirrored direction base

		const speeds = Array.from({ length: count }, (_, i) => {
				if (count === 1) return baseSpeed;
				if (count === 2) return baseSpeed * (-1);
				if (count === 3) return baseSpeed * 0; // [-1, 0, +1]
				});

		return {
					symbol: random(orbitPool),
					sides : int(random(3, 10)),
					angle : random(360),
					radius: random(width * 0.1, width * 0.4),
					baseSpeed,
					speeds, // list of speeds for sublayers
					count,
					phase : random(360),
				};
		});
	}


function planet(sym, sides, max_radius, speed, phase) {
	let r = (frameCount * speed) % max_radius;
	const angles = getAngles(sides);
	ctx.save();
	// center & rotate the whole ring
	ctx.translate(width/2, height/2);
	ctx.rotate( frameCount * speed + phase);
	// draw ring once
	// 1️⃣ draw the semi-transparent polygon (the “rail”)
	ctx.strokeStyle = `rgba(255,215,0,${0.2})`;
	ctx.beginPath();
	angles.forEach((a,i) => {
			const x = Math.cos(a) * r;
			const y = Math.sin(a) * r;
			if (i === 0) ctx.moveTo(x,y);
			else ctx.lineTo(x,y);
			});
	ctx.closePath();
	ctx.stroke();

	// draw runes
	ctx.fillStyle = `rgba(255,215,0,${r / maxR})`;
	angles.forEach(a => {
			const x = Math.cos(a) * r;
			const y = Math.sin(a) * r;
			ctx.save();
			ctx.translate(x, y);
			ctx.rotate(frameCount * speed);
			ctx.fillText(sym, 0, 0);
			ctx.restore();
			});
	ctx.restore();
	}


function planet_group(sym, sides, base_radius, base_speed, phase, count = 3) {
	for (let i = 0; i < count; i++) {
		const radius = base_radius * (0.6 + 0.2);  // spread out
		const speed  = base_speed * (1 + 0.3 * i );  // vary speed/direction a bit
		planet(sym, sides, radius, speed, phase); // slight phase offset per ring
		planet(sym, sides, radius, -speed, phase); // slight phase offset per ring
		planet(sym, sides, radius, 0, phase); // slight phase offset per ring
		}
	}

function sol(sym, spin = solSpinSpeed, base = solBaseScale, beat = solBeatAmp) {
		push();
		translate(width / 2, height / 2);

		// 1️⃣ rotation
		rotate(frameCount * spin);

		// 2️⃣ heartbeat scaling
		const pulse = 1 + abs(beat * (sin(frameCount * 2) + sin(frameCount * 3)+ sin(frameCount * 5) )); // 4 = beats per rotation cycle
		const ts    = base * width * pulse;
		textSize(ts);

		// 3️⃣ aura (two translucent strokes behind the main rune)
		fill(255, 215, 0, 50);     // faint golden halo
		glowColor = color(255, 215, 0, 70);
		glow(glowColor, 10);

		fill(255, 215, 0, 200);  // bright core glyph
		text(sym, 0, 0);

		pop();
		}


function setup () {
		const size = Math.max(window.innerWidth, window.innerHeight)//, 420);
		let canvas = createCanvas(size, size);
		canvas.parent('p5-holder');
		angleMode(DEGREES);
		textAlign(CENTER, CENTER);
		textSize(size * 0.18);
		noStroke();
		initSymbols();
		frameRate(25);
		}

function windowResized() {
		// Responsiveness: redraw canvas on resize
		const size = Math.min(window.innerWidth, window.innerHeight, 420);
		resizeCanvas(size, size, true);
		textSize(size * 0.18);
		}

function glow(glowColor, blurriness) {
		drawingContext.shadowColor = glowColor;
		drawingContext.shadowBlur = blurriness;
		}

let frame = 0;
let angle = 1.1;

function draw () {
		clear();
		if (backgroundAlpha < maxAlpha) {
				backgroundAlpha += 5; // Increase speed as you like
				if (backgroundAlpha > maxAlpha) backgroundAlpha = maxAlpha;
				}
		background(0, backgroundAlpha);


		// Center symbol (sun) – strong gold
		//fill(255, 215, 100, 100);
		//textSize(width * 0.18);
		//text(centerSymbol, 0, 0);
		sol(centerSymbol);

		const size = Math.max(window.innerWidth, window.innerHeight)*2//, 420);

		// Orbits: glowing gold
		//fill(255, 215, 0, 90);
		orbitSymbols.forEach(o => {
			const scaled_radius = o.radius * (width / 420);
			planet_group(o.symbol, o.sides, scaled_radius, o.speeds, o.phase);
			});
		}



/* --------------------  3. CONTROL DEL LOADER  -------------------- */
const loader   = document.getElementById('loader');
const fullPage = document.getElementById('FullPage');

function showLoader () {
		loader.style.display   = 'flex';
		fullPage.style.display = 'none';
		initSymbols(); // nuevo diseño en cada ciclo
		loop();        // reanuda animación
		}

function hideLoader () {
		loader.style.display   = 'none';
		fullPage.style.display = 'block';
		noLoop();      // detiene animación
		}

/* --------------------  4. ENLACE DE EVENTOS  -------------------- */
// 4.1 – Ocultamos loader tras la carga inicial completa.
window.addEventListener('load', hideLoader);

// 4.2 – Formularios que recargan → muestran loader.
document.querySelectorAll('form')
		.forEach(f => f.addEventListener('submit', showLoader));

// 4.3 – Botones con navegación por JS.
document.querySelectorAll('button')
		.forEach(b => {
		  if (b.onclick && b.onclick.toString().includes('window.location.href')) {
			b.addEventListener('click', showLoader);
		  }
		});

// 4.4 – Botón especial con generateList (ajústalo a tu selector real).
const listBtn = document.querySelector('button[onclick^="generateList"]');
if (listBtn) listBtn.addEventListener('click', showLoader);

/* --------------------  5. SÍMBOLO ALEATORIO EN #spinner  --------- */
document.addEventListener('DOMContentLoaded', () => {
		const spin = document.getElementById('spinner');
		if (spin) spin.textContent = spinnerChars[Math.floor(Math.random() * spinnerChars.length)];
		});
