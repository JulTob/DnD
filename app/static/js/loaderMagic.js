/* MagicLoader.js  ✨
 * Animación de círculo mágico + control del loader
 * Autor: ChatGPT (o3)
 */

// ----  GLOBALS  -------------------------------------------------
let solBaseScale = 0.18;
let solBeatAmp   = 0.10;   // 8 % size pulsation
let solSpinSpeed = 0.0;    // degrees per frame   (tweak to taste)

let backgroundAlpha = 0;  // Start fully transparent
const maxAlpha = 255;

let polygons = [];          // will hold every planet/poly
const MIN_SIDES = 3;
const MAX_SIDES = 12;

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
		orbitSymbols = Array.from(
				{ length: int(random(4, 12)) },
				() => ({
					symbol: random(orbitPool),
					sides : int(random(3, 10)),         // ← 3 to 12 sides
					angle : random(360),
					radius: random(width * 0.1, width*0.8 ),
					speed : random(-2.0, 2.0),
					phase : random(360),
					}),
				);
		}
function planet(sym, sides, max_radius, speed, phase) {
  push();
	// center & rotate the whole ring
	translate(width/2, height/2);
	rotate( frameCount * speed + 2*phase);
	radius = frameCount * speed % max_radius
	// 1️⃣ draw the semi-transparent polygon (the “rail”)
	stroke(255, 215, 0, 255* (1-abs(cos(frameCount / sides +phase))));  // gold with 60/255 alpha
	noFill();
	beginShape();
	  for (let i = 0; i < sides; i++) {
		let ang = i * 360 / sides;
		let x   = cos(ang) * radius;
		let y   = sin(ang) * radius;
		vertex(x, y);
	  }
	endShape(CLOSE);

	// 2️⃣ draw the translucent runes at each vertex
	const txtSz = max_radius * 0.025 * (2-sin(frameCount / sides +phase)) ;          // tweak size if you like
	textSize(txtSz);
	noStroke();
	for (let i = 0; i < sides; i++) {
	  let ang = i * 360 / sides;
	  let x   = cos(ang) * radius;
	  let y   = sin(ang) * radius;

	push();
        // center on this vertex
        translate(x, y);
        // rotate around its own center:
        // we add i*offset so runes don't all line up in lock-step
        rotate(frameCount * speed * i + radians(i * (360 / sides)));
        fill(255, 215, 0, int(map(radius, 0, max_radius, 10, 255)));
        text(sym, 0, 0);
      pop();

	}
  pop();
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
				planet(o.symbol, o.sides, o.radius * (width/420), o.speed, o.phase);
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
