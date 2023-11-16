
import random
import npc_class as NPC
import dnd

def Dice(D=6,N=1):
    return dnd.Dice(D=D,N=N)

def PlotHook(npc):
    Hooks = [
        "I received a message from a God, but it was unclear. I must find a long forgotten shrine to talk to him again.", 
        "I must find a rare alchemist element to make a medicine needed for my kind.",
        "I was chosen to defeat the enemy of my kind.",
        "I must contact a spirit that belongs to this place.",
        "I lost somebody. There may be a way to have them back in this place.",
        "There is something trapped in this place. I seek to liberate them.",
        "There is something trapped in this place. I seek to keep it that way.",
        "I'm trapped. Could you please help me?",
        "I'm infiltrating a corrupt organization to take it down from the inside.",
        "I'm looking for a child that was taken from my kind.",
        "I am a gladiator entertainer. I need to give a good spectacle to provide for my kind.",
        "I shall prove myself in the Arena.",
        "I shall gain fame and fortune in the Arena.",
        "One from my kind was killed. I seek revenge.",
        "One from my kind was harmed. I seek compensation.",
        "I was slaved for a long time. I seek revenge.",      
        "I was slaved for a long time. I seek to liberate others in chains.",      
        "A partner was taken in battle. I will liberate them or die trying.",
        "One from my kind has been taken by slavers. I will liberate them or die trying.",
        "I am connected to the spirits of my kind. They carry a purpose for me that I shall carry on my shoulders.",
        "I lost all hope in my civilization. I shall make something new.",
        "I lost my purpose long ago. I'm looking for something new to care for.",
        "My kind carries an ancient curse. I shall cleanse our souls.",
        "My kind is alienated in these lands. We just try to survive, but anger folows wherever we go. ",
        "I run away from the opression of my kind",
        "I fight against the opression of my kind",
        "My kind is under repression. I aim to liberate them.",
        "I was unjustly imprisoned by a rival, I will get my revenge and then more. ",
        "I've been away of home to fight a war. I now want to go back to my loved ones.",
        "I was promised for a convenience marriage. I decided to run away.",
        "I'm the legacy of a tyrant. I am correcting their sins.",
        "My family was victim to a great injustice. I seek restitution to my name.",
        "My family is guilty of a great crime. I'm trying to ammend this injustice.",
        "I was excommunicated. I'm redeeming myself in the eyes of my gods. ",
        "I'm condemned to hell. I want redemption.",
        "I'm already condemned to the hells. I might as well earn it.",
        "These are my hunting territories. You are now my prey.",
        "I am the tyrant of these lands",
        "I must visit all the oceans of the world and behold the ships that sail there.",
        "I was tricked by a smuggler who stole something precious from me. I will find that thief.",
        "After one last job, I will retire from the business.",
        "I owe a debt that cannot be repaid in gold.",
        "I intend to become the leader of the kind that I belong to.",
        "My most valuable possession was stolen from me, and I burn with the desire to recover it.",
        "My vessel was stolen from me, and I burn with the desire to recover it.",
        "My familiar was stolen from me, and I burn with the desire to recover it.",
        "My sword was stolen from me, and I burn with the desire to recover it.",
        "My loved one was kidnapped from me, and I burn with the desire to recover them.",
        "An item with personal value was stolen from me, and I burn with the desire to recover it.",
        "Someone I love was killed by a rival kind, and I will have revenge.",
        "I love someone from another kind, but the relationship is forbidden.",
        "I was exiled for a crime I didn't commit.",
        "I keep my thoughts and discoveries in a journal. My journal is my legacy. I just lost it!",
        "A monster that slaughtered dozens of innocent people spared my life, and I don’t know why. I am certain it follows me since.",
        "I protect those who cannot protect themselves.",
        "I have a family, but I have no idea where they are. One day, I hope to see them again.",
        "Recruited into a lord's army, I rose to leadership and was commended for my heroism. Now I fight for them.",
        "A celestial, fey, or similar creature gave me a blessing or revealed my secret origin.",
        "I'm breaking into a tyrant's castle to steal weapons to arm the people.",
        "I lead a militia to fight off an invading army.",
        "I steal from merchants to help the poor.",
        "I'm the last hope against a terrible monster.",
        "I want to save people of a comming disaster.",
        "I stand up to a tyrant's agents.",
        "I must repay my village's debt.",
        "My destiny awaits me at the bottom of a particular pond in the Feywild.",
        "The gods saved me during a terrible storm, and I will honor their gift.",
        "I will hunt the many famous beasts of this land.",
        "I will fish the many famous waters of this land.",
        "Someone else's greed destroyed my livelihood, and I will be compensated.",
        "I lost something important in the deep sea, and I intend to find it.",
        "I have a tail like that of a dog or another animal, as a punishment from a Fey for an accidental insult.",
        "I have a weakness for the exotic beauty of the people of these lands.",
        "I do everything for those who were taken from me.",
        "I am exceptional. I do this because no one else can, and no one can stop me.",
        "I stand in opposition, lest the wicked go unopposed.",
        "I've seen too many in need. I must not fail them as everyone else has.",
        "What I do, I do for the world. The people don't realize how much they need me.",
        "I do everything for my kind. My first thought is keeping them safe.",
        "I once satirized a noble who still wants my head. It was a mistake that I will likely repeat.",
        "I would do anything for the other members of my old troupe.",
        "I will do anything to prove myself superior to my hated rival.",
        "I want to be famous, whatever it takes.",
        "Someone stole an object precious to me, and someday I'll get it back.",
        "Someone I loved died because of I mistake I made. That will never happen again.",
        "I'm guilty of a terrible crime. I hope I can redeem myself for it.",
        "I will become the greatest thief that ever lived.",
        "Something important was taken from me, and I aim to steal it back.",
        "My ill-gotten gains go to support my kind.",
        "I'm trying to pay off an old debt I owe to a generous benefactor.",
        "I swindled and ruined a person who didn't deserve it. I seek to atone for my misdeeds but might never be able to forgive myself.",
        "A powerful person killed someone I love. Some day soon, I'll have my revenge.",
        "I come from a noble family, and one day I'll reclaim my lands and title from those who stole them from me.",
        "Somewhere out there, I have a child who doesn't know me. I'm making the world better for him or her.",
        "I owe everything to my mentor – a horrible person who's probably rotting in jail somewhere.",
        "I fleeced the wrong person and must work to ensure that this individual never crosses paths with me or those I care about.",
        "I hope to bring prestige to a library.",
        "I hope to bring prestige to a museum.",
        "I hope to bring prestige to a university.",
        "I won't sell an art object that has historical significance.",
        "I won't sell an art object that is one of a kind.",
        "I won't sell a treasure that has historical significance.",
        "I won't sell a treasure that is one of a kind.",
        "I have a friendly rival. Only one of us can be the best, and I aim to prove it's me.",
        "I want to find my mentor, who disappeared on an expedition some time ago.",
        "Ever since I was a child, I've heard stories about a lost city. I aim to find it, learn its secrets, and earn my place in the history books.",
        "I'm under a curse.",
        "I'm the Protector of this Land",
        "I'm guarding something of great importance.",
        "I'm protecting someone of great importance.",
        "I'm looking for a special thing",
        "I I just want to have fun",
        "I'm looking for someone",
        "I want to get rich",
        "I'm selling something",
        "I'm buying something",
        "I want to ammend a mistake.",
        "I want to recuperate my honor",
        "I'm protecting my kind",
        "I want to prove myself",
        "I'm curious",
        "I'm protecting my interests",
        "I am lost",
        "I am a freedomfighter.",
        "I want to topple a tyrant.",
        "I fight to preserve order",
        "I am in pilgrimage",
        "I lost my home, and I'm looking for a new life.",
        "A higher power commanded a very important mission.",
        "I'm just following orders.",
        "I am injured. ",
        "I'm in a forbidden or impossible relationship. ",
        "I have a legacy to mantain",
        "I have a great rival",
        "I pursue a goal that breaks tradition or law",
        "I am in debt.",
        "I lead an uprising.",
        "Feels loyalty to two opposing causes.",
        "Feels loyalty to two opposing kinds.",
        "Has a crisis of faith.",
        "Is looking for revenge",
        "Is trying to solve a failure.",
        "Is trying to solve a tragedy.",
        "Is standing up for those who are not equipped to stand up for themselves.",
        "They keep a great secret.",
        "They need to unveil a great secret.",
        "I am bored.",
        "I am hungry.",
        "I am trapped.",
        "I want to create something.",
        "I am running from justice.",
        "I am running from justice for a crime I didn't commit.",
        "I have to make a very difficult choice",
        "I serve an unethical and corrupt organization.",
        "I would die to recover an ancient relic of my faith that was lost long ago.",
        "I will someday get revenge on the corrupt temple hierarchy who branded me a heretic.",
        "I owe my life to the priest who took me in when my parents died.",
        "Everything I do is for the common people.",
        "I will do anything to protect the holy site where I serve.",
        "I seek to preserve a sacred text that my enemies consider heretical and seek to destroy.",
        "My mentor gave me a journal filled with lore and wisdom. Losing it would devastate me.",
        "Having lived among the people of a primeval tribe or clan, I long to return and see how they are faring.",
        "Years ago, tragedy struck the members of an isolated society I befriended, and I will honor them.",
        "I want to learn more about a particular humanoid culture that fascinates me.",
        "I seek to avenge a clan that was wiped out.",
        "I seek to avenge a tribe that was wiped out.",
        "I seek to avenge a kingdom that was wiped out.",
        "I seek to avenge an empire that was wiped out.",
        "I seek to avenge my kind, that was wiped out.",
        "I have a trinket that I believe is the key to finding a long-lost society.",
        "I will overcome a rival and prove myself their better.",
        "My mistake got someone hurt. I'll never make that mistake again.",
        "I will be the best for the honor and glory of my home.",
        "A proud noble once gave me a horrible beating, and I will take my revenge on any bully I encounter.",
        "The tyrant who rules my land will stop at nothing to see me killed.",
        "My kind has a history of practicing the dark arts. I dabbled once and felt something horrible clutch at my soul, whereupon I fled in terror.",
        "An apparition that has haunted my family for generations now haunts me. I don’t know what it wants, and it won’t leave me alone.",
        "An oni took my sibling one cold, dark night, and I was unable to stop it.",
        "I was cursed with lycanthropy. I am now haunted by the innocents I slaughtered.",
        "My torment drove away the person I love. I strive to win back the love I’ve lost.",
        "I have a child to protect. I must make the world a safer place for them.",
        "I am searching for spiritual enlightenment.",
        "I am the caretaker of an ancient ruin.",
        "I am the caretaker of an ancient relic.",
        "I have great insight into a great evil that only I can destroy.",
        "Should my discovery come to light, it could bring ruin to the world.",
        "I entered seclusion to hide from the ones who might still be hunting me. I must someday confront them.",
        "I am a pilgrim in search of a person, place, or relic of spiritual significance.",
        "A fiend possessed you as a child. You were locked away but escaped. The fiend is still inside you, but now you try to keep it locked away.",
        "I owe a debt I can never repay to the person who took pity on me.",
        "I escaped my life of poverty by robbing an important person, and I'm wanted for it.",
        "Grand Designs. You are working on plans and schematics for a new, very fast ship. You must examine as many different kinds of vessels as possible to help ensure the success of your design.",
        "I must find a kind of wood rumored to possess magical qualities.",
        "I will craft a boat capable of sailing through the most dangerous of storms.",
        "A kraken destroyed my ship; its teeth shall adorn my hearth.",
        "A dragon destroyed my town; its teeth shall adorn my armour.",
        "A monster destroyed my town; its teeth shall adorn my armour.",
        "A monster destroyed my home; I will find it, and destroy it.",
        "I work to preserve a library, university, scriptorium, or monastery.",
        "I have an ancient text that holds terrible secrets that must not fall into the wrong hands.",
        "I was cheated out of my fair share of the profits, and I want to get my due.",
        "I've been searching my whole life for the answer to a certain question.",
        "Ruthless pirates murdered my captain and crewmates, plundered our ship, and left me to die. Vengeance will be mine.",
        "I must ran twenty-five miles without stopping to warn my clan of an approaching horde.",
        "I will bring terrible wrath down on the evildoers who destroyed my homeland.",
        "I am the last of my kind, and it is up to me to ensure their names enter legend.",
        "I suffer awful visions of a coming disaster and will do anything to prevent it.",
        "It is my duty to raise children to mantain my kind.",
        "I face danger and evil to offset an unredeemable act in my past.",
        "I'm searching for a friend captured by an elusive enemy.",
        "My commander betrayed my unit, and I will have revenge.",
        ""]
    return random.choice(Hooks)


def Trait(npc):
    background=npc.background
    Traits = []
    Traits += [
        # Moral Compass
        "Virtuous",
        "Principled",
        "Honorable",
        "Unprincipled",
        "Dishonorable",
        
        # Personal Goals
        "Power",
        "Knowledge",
        "Peace",
        "Chaos",
        "Revenge",
        "Justice",
        
        # Relationship with Society
        "Conformist",
        "Rebel",
        "Outsider",
        "Leader",
        "Follower",
        "Anarchist",
        
        # Primal Instincts
        "Survivalist",
        "Protector",
        "Predator",
        "Opportunist",
        "Guardian",
        "Destroyer",
        
        # Complex Alignments
        "Benevolent Dictator",
        "Reluctant Hero",
        "Martyr",
        "Machiavellian",
        "Nihilist",
        "Altruist",
        
        # Belief Systems
        "Theist",
        "Atheist",
        "Agnostic",
        "Spiritualist",
        "Skeptic",
        "Zealot",
        
        # Existential Alignments
        "Existentialist",
        "Absurdist",
        "Fatalist",
        "Optimist",
        "Pessimist",
        "Realist"
  
        "I am optimistic, seeing events in the most positive light.",   
        "If you do me an injury, I will crush you, ruin your name, and salt your fields.",
        "My favor, once lost, is lost forever.",
        "Despite my noble birth, I do not place myself above other folk. We all have the same blood.",
        "I don't like to get my hands dirty, and I won't be caught dead in unsuitable accommodations.",
        "I take great pains to always look my best and follow the latest fashions.",
        "No one could doubt by looking at my regal bearing that I am a cut above the unwashed masses.",
        "The common folk love me for my kindness and generosity.",
        "My eloquent flattery makes everyone I talk to feel like the most wonderful and important person in the world.",
        "I sometimes stay up all night listening to the ghosts of my fallen enemies.",
        "I become irrational when innocent people are hurt.",
        "I hold grudges and have difficulty forgiving others.",
        "My intensity can drive others away.",
        "I find civilian life difficult and struggle to say the right thing in social situations.",
        "I grow combative and unpredictable when I drink.",
        "Fear leads to tyranny, and both must be eradicated.",
        "I must set an example of hope for those who have given up.",
        "I. Will. Finish. The. Job.",
        "When the sea is within my sight, my mood is jovial and optimistic.",
        "I become cantankerous and quiet in the rain.",
        "I am always working on some project or other.",
        "I am dependable.",
        "I enjoy being out in nature; poor weather never sours my mood.",
        "I prefer to solve problems without violence, but I finish fights decisively.",
        "I laugh loudly and see the humor in stressful situations.",
        "I speak rarely but mean every word I say.",
        "By my words and actions, I often bring shame to my family.",
        "In fact, the world does revolve around me.",
        "I have an insatiable desire for carnal pleasures.",
        "I too often hear veiled insults and threats in every word addressed to me, and I'm quick to anger.",
        "I hide a truly scandalous secret that could ruin my family forever.",
        "I secretly believe that everyone is beneath me.",
        "The common folk must see me as a hero of the people.",
        "My loyalty to my sovereign is unwavering.",
        "I am in love with the heir of a family that my family despises.",
        "Nothing is more important than the other members of my family.",
        "My house's alliance with another noble family must be sustained at all costs.",
        "I will face any challenge to win the approval of my family.",
        "If you do me an injury, I will crush you, ruin your name, and salt your fields.",
        "My favor, once lost, is lost forever.",
        "Despite my noble birth, I do not place myself above other folk. We all have the same blood.",
        "I don't like to get my hands dirty, and I won't be caught dead in unsuitable accommodations.",
        "I take great pains to always look my best and follow the latest fashions.",
        "No one could doubt by looking at my regal bearing that I am a cut above the unwashed masses.",
        "The common folk love me for my kindness and generosity.",
        "My eloquent flattery makes everyone I talk to feel like the most wonderful and important person in the world.",
        "Don't expect me to save those who can't save themselves. It is nature's way that the strong thrive and the weak perish.",
        "Violence is my answer to almost any challenge.",
        "I am slow to trust members of other races, tribes, and societies.",
        "I remember every insult I've received and nurse a silent resentment toward anyone who's ever wronged me.",
        "There's no room for caution in a life lived to the fullest.",
        "I am too enamored of ale, wine, and other intoxicants.",
        "I was, in fact, raised by wolves.",
        "I feel far more comfortable around animals than people.",
        "I'm always picking things up, absently fiddling with them, and sometimes accidentally breaking them.",
        "I place no stock in wealthy or well-mannered folk. Money and manners won't save you from a hungry owlbear.",
        "I have a lesson for every situation, drawn from observing nature.",
        "I once ran twenty-five miles without stopping to warn my clan of an approaching orc horde. I'd do it again if I had to.",
        "I watch over my friends as if they were a litter of newborn pups.",
        "I'm driven by a wanderlust that led me away from home.",
        "I can't keep a secret to save my life, or anyone else's."
        "I speak without really thinking through my words, invariably insulting others."
        "I overlook obvious solutions in favor of complicated ones.",
        "Unlocking an ancient mystery is worth the price of a civilization.",
        "Most people scream and run when they see a demon. I stop and take notes on its anatomy.",
        "I am easily distracted by the promise of information.",
        "I sold my soul for knowledge. I hope to do great deeds and win it back.",
        "My life's work is a series of tomes related to a specific field of lore.",
        "I'm convinced that people are always trying to steal my secrets.",
        "I am horribly, horribly awkward in social situations.",
        "I… speak… slowly… when talking… to idiots,… which… almost… everyone… is… compared… to me.",
        "I'm willing to listen to every side of an argument before I make my own judgment.",
        "There's nothing I like more than a good mystery.",
        "I'm used to helping out those who aren't as smart as I am, and I patiently explain anything and everything to others.",
        "I've read every book in the world's greatest libraries – or I like to boast that I have.",
        "I use polysyllabic words that convey the impression of great erudition.",
        "My pride will probably lead to my destruction.",
        "I can't help but pocket loose coins and other trinkets I come across.",
        "Once I start drinking, it's hard for me to stop.",
        "Once someone questions my courage, I never back down no matter how dangerous the situation.",
        "I'll say anything to avoid having to do extra work.",
        "I follow orders, even if I think they're wrong.",
        "In a small town, I have a paramour whose eyes nearly stole me from my purpose.",
        "I'll always remember my first ship.",
        "The ship is most important – crewmates and captains come and go.",
        "I'm loyal to my captain first, everything else second.",
        "I don't know when to throw something away. You never know when it might be useful again.",
        "I repair broken things to redeem what's broken in myself.",
        "Much of the treasure I claim will be used to enrich my community.",
        "I don't mind getting my hands dirty.",
        "I have an endless supply of cautionary tales related to the sea.",
        "A pipe, an ale, and the smell of the sea: paradise.",
        "I'm not afraid of hard work—in fact, I prefer it.",
        "I love sketching and designing objects.",
        "I love sketching and designing objects, especially traps.",
        "I love sketching and designing objects, especially boats.",
        "I love sketching and designing objects, especially weapons.",
        "I love sketching and designing objects, especially constructs.",
        "I love sketching and designing objects, especially magic items.",
        "I thrive under pressure.",
        "I'm extremely fond of puzzles.",
        "I love talking and being heard more than I like to listen.",
        "Mysteries of the Deep. You experienced an encounter with a possibly divine being while sailing alone. Work with your DM to determine the secret about the deep waters of the sea that this entity revealed to you.",
        "Low Places. You have contacts in the smuggling outfits along the coast; you occasionally repair the criminals' ships in exchange for coin and favors.",
        "Master of Armaments. You specialized in designing and mounting defenses for the navy. You easily recognize and determine the quality of such items.",
        "Favored. Gave a great advice to a merchant, which saved it from ruin. You have a standing invitation to visit the merchant's distant mansion.",
        "Solid and Sound. You patched up a war galley and prevented it from sinking. The local navy regards you as a friend.",
        "Though I act charming, I feel nothing for others and don't know what friendship is.",
        "Few people know the real me.",
        "I struggle to trust the words of others.",
        "I believe everyone has a price and am cynical toward those who present themselves as virtuous.",
        "I tend to assess my relationships in terms of profit and loss.",
        "Lying is reflexive, and I sometimes engage in it without realizing.",
        "I give most of my profits to a charitable cause, and I don't like to brag about it.",
        "I become wistful when I see the sun rise over the ocean.",
        "I enjoy doing things others believe to be impossible.",
        "I love gold but won't cheat a friend.",
        "Nothing rattles me; I have a lie for every occasion.",
        "I never stop smiling.",
        "I think of everything in terms of monetary value.",
        "I'd rather eat my armor than admit when I'm wrong.",
        "I obey the law, even if the law causes misery.",
        "My hatred of my enemies is blind and unreasoning.",
        "I made a terrible mistake in battle that cost many lives – and I would do anything to keep that mistake secret.",
        "I have little respect for anyone who is not a proven warrior.",
        "The monstrous enemy we faced in battle still leaves me quivering with fear.",
        "I fight for those who cannot fight for themselves.",
        "Those who fight beside me are those worth dying for.",
        "I'll never forget the crushing defeat my kind suffered or the enemies who dealt it.",
        "My honor is my life.",
        "Someone saved my life on the battlefield. To this day, I will never leave a friend behind.",
        "I would still lay down my life for the people I served with.",
        "I face problems head-on. A simple, direct solution is the best path to success.",
        "I have a crude sense of humor.",
        "I enjoy being strong and like breaking things.",
        "I can stare down a hell hound without flinching.",
        "I'm full of inspiring and cautionary tales from my military experience relevant to almost every combat situation.",
        "I've lost too many friends, and I'm slow to make new ones.",
        "I'm haunted by memories of war. I can't get the images of violence out of my mind.",
        "I'm always polite and respectful.",
        "People who can't take care of themselves get what they deserve.",
        "It's not stealing if I need it more than someone else.",
        "I'd rather kill someone in their sleep than fight fair.",
        "I will never fully trust anyone other than myself.",
        "Gold seems like a lot of money to me, and I'll do just about anything for more of it.",
        "If I'm outnumbered, I will run away from a fight.",
        "No one else should have to endure the hardships I've been through.",
        "I owe my survival to another urchin who taught me to live on the streets.",
        "I sponsor an orphanage to keep others from enduring what I was forced to endure.",
        "My town or city is my home, and I'll fight to defend it.",
        "My secret could get me expelled from my kind.",
        "My kind and blood line make me the best!",
        "I'm obsessed with conspiracy theories and worried about secret societies and hidden demons.",
        "I'm fixated on following official protocols.",
        "I'm determined to impress the leaders of my faction, and to become a leader myself.",
        "My organization must evolve, and I'll lead the evolution.",
        "I don't care about the organization as a whole, but I would do anything for my old mentor.",
        "I never forget an insult against me.",
        "I'm always looking to improve efficiency.",
        "I like keeping secrets and won't share them with anyone.",
        "I'd risk too much to uncover a lost bit of knowledge.",
        "I let my need to win arguments overshadow friendships and harmony.",
        "I am dogmatic in my thoughts and philosophy.",
        "I harbor dark, bloodthirsty thoughts that my isolation and meditation failed to quell.",
        "Now that I've returned to the world, I enjoy its delights a little too much.",
        "I entered seclusion because I loved someone I could not have.",
        "I'm still seeking the enlightenment I pursued in my seclusion, and it still eludes me.",
        "I am working on a grand philosophical theory and love sharing my ideas.",
        "I often get lost in my own thoughts and contemplation, becoming oblivious to my surroundings.",
        "I connect everything that happens to me to a grand, cosmic plan.",
        "I'm oblivious to etiquette and social expectations.",
        "I feel tremendous empathy for all who suffer.",
        "The leader of my community had something wise to say on every topic, and I am eager to share that wisdom.",
        "I am utterly serene, even in the face of disaster.",
        "I've been isolated for so long that I rarely speak, preferring gestures and the occasional grunt.",
        "I needed to commune with nature, far from civilization.",
        "I needed a quiet place to work on my art, literature, music, or manifesto.",
        "I retreated from society after a life-altering event.",
        "I talk to spirits that no one else can see.",
        "I am a purveyor of doom and gloom who lives in a world without hope.",
        "I have an addiction.",
        "I feel no compassion for the dead. They’re the lucky ones.",
        "I assume the worst in people.",
        "I have certain rituals that I must follow every day. I can never break them.",
        "There’s evil in me, I can feel it. It must never be set free.",
        "A terrible guilt consumes me. I hope that I can find redemption through my actions.",
        "I would sacrifice my life and my soul to protect the innocent.",
        "I put no trust in divine beings.",
        "I refuse to become a victim, and I will not allow others to be victimized.",
        "I expect danger around every corner.",
        "I don’t talk about the thing that torments me. I’d rather not burden others with my curse.",
        "I live for the thrill of the hunt.",
        "I spend money freely and live life to the fullest, knowing that tomorrow I might die.",
        "I like to read and memorize poetry. It keeps me calm and brings me fleeting moments of happiness.",
        "I don't run from evil. Evil runs from me.",
        "You did terrible things to avenge the murder of someone you loved. You became a monster, and it haunts your waking dreams.",
        "You opened an eldritch tome and saw things unfit for a sane mind. You burned the book, but its words and images are burned into your psyche.",
        "A hag kidnapped and raised you. You escaped, but the hag still has a magical hold over you and fills your mind with evil thoughts.",
        "I was born under a dark star. I can feel it watching me, coldly and distantly. Sometimes it beckons me in the dead of night.",
        "I'm well known for my work, and I want to make sure everyone appreciates it. I'm always taken aback when people haven't heard of me.",
        "I don't part with my money easily and will haggle tirelessly to get the best deal possible."
        "I like to talk at length about my profession.",
        "I'm rude to people who lack my commitment to hard work and fair play.",
        "I'm full of witty aphorisms and have a proverb for every occasion.",
        "I always want to know how things work and what makes people tick.",
        "I'm a snob who looks down on those who can't appreciate fine art.",
        "I believe that anything worth doing is worth doing right. I can't help it – I'm a perfectionist.",
        "I change my mood or my mind as quickly as I change key in a song.",
        "I'll settle for nothing less than perfection.",
        "I get bitter if I'm not the center of attention.",
        "I love a good insult, even one directed at me.",
        "Nobody stays angry at me or around me for long, since I can defuse any amount of tension.",
        "I'm a hopeless romantic, always searching for that 'special someone'.",
        "Whenever I come to a new place, I collect local rumors and spread gossip.",
        "I know a story relevant to almost every situation.",
        "I have trouble trusting in my allies.",
        "Secretly, I believe that things would be better if I were a tyrant lording over the land.",
        "I have a weakness for the vices of the city, especially hard drink.",
        "The people who knew me when I was young know my shameful secret, so I can never go home again.",
        "I'm convinced of the significance of my destiny, and blind to my shortcomings and the risk of failure.",
        "I wish my childhood sweetheart had come with me to pursue my destiny.",
        "My tools are symbols of my past life, and I carry them so that I will never forget my roots.",
        "I worked the land, I love the land, and I will protect the land.",
        "I get bored easily. When am I going to get on with my destiny?",
        "I misuse long words in an attempt to sound smarter.",
        "Thinking is for other people. I prefer action.",
        "I'm confident in my own abilities and do what I can to instill confidence in others.",
        "I have a strong sense of fair play and always try to find the most equitable solution to arguments.",
        "When I set my mind to something, I follow through no matter what gets in my way.",
        "If someone is in trouble, I'm always ready to lend help.",
        "I judge people by their actions, not their words.",
        "I am obsessed with catching an elusive beast, often to the detriment of other pursuits.",
        "I work hard, but I play harder.",
        "I am inclined to tell long-winded stories at inopportune times.",
        "I have lived a hard life and find it difficult to empathize with others.",
        "I become depressed and anxious if I'm away from the sea too long.",
        "I am judgmental, especially of those I deem homebodies or otherwise lazy.",
        "Luck favors me, and I take risks others might not.",
        "I dislike bargaining; state your price and mean it.",
        "I work hard; nature offers no handouts.",
        "I laugh heartily, feel deeply, and fear nothing.",
        "Rich folk don't know the satisfaction of hard work.",
        "I need long stretches of quiet to clear my head.",
        "My friends are my crew; we sink or float together.",
        "I am unmoved by the wrath of nature.",
        "I'm always changing my mind-well, almost always.",
        "I have many vices and tend to indulge them.",
        "I never give away anything for free and always expect something in return.",
        "I'm forgetful. Sometimes I can't remember even the simplest things.",
        "I'm a kleptomaniac who covets shiny, sparkling treasure.",
        "I'm always operating under a tight timeline, and I'm obsessed with keeping everything on schedule.",
        "I think the whole multiverse is out to get me.",
        "I easily lose track of time. My poor sense of time means I'm always late.",
        "I feel indebted to a witch for giving me a home and a purpose.",
        "I feel indebted to a fae for giving me a home and a purpose.",
        "I'm drawn to the Feywild and long to return there, if only for a short while.",
        "The Witchlight Carnival (Halloween) feels like home to me.",
        "I can't bring myself to harm a Fey creature, because I consider myself one.",
        "I can't bring myself to harm a Fey creature, I fear the repercussions.",
        "A trusted friend is the most important thing in the multiverse to me.",
        "I do what I can to protect the natural world.",
        "I find magic in all its forms to be compelling. The more magical a place, the more I am drawn to it.",
        "I would never break my word.",
        "Rule of Three. Everything in the multiverse happens in threes. I see the 'rule of three' everywhere.",
        "I can't bring myself to trust most adults.",
        "I live by my own set of weird and wonderful rules.",
        "When I have a new idea, I get wildly excited about it until I come up with another, better idea.",
        "I have never lost my childlike sense of wonder.",
        "Wherever I go, I try to bring a little of the warmth and tranquility of home with me.",
        "Good music makes me weep like a baby.",
        "Like a nomad, I can't settle down in one place for very long.",
        "I'm haunted by fey laughter that only I can hear, though I know it's just my mind playing tricks on me.",
        "Flowers wilt in my presence.",
        "Flowers bloom in my presence.",
        "My skin sparkles in sunlight.",
        "My skin sparkles in moonlight.",
        "I have a sweet scent, like that of nectar or honey",
        "My eyes swirl with iridescent colors.",
        "I consider the adherents of other gods to be deluded innocents at best, or ignorant fools at worst.",
        "I don't take kindly to some of the actions and motivations of the people of this land, because these folk are different from me.",
        "I have a weakness for the new intoxicants and other pleasures of this land.",
        "I pretend not to understand the local language in order to avoid interactions I would rather not have.",
        "I am secretly (or not so secretly) convinced of the superiority of my own culture over that of this foreign land.",
        "Though I had no choice, I lament having to leave my loved ones behind. I hope to see them again one day.",
        "I'm fascinated by the beauty and wonder of this new land.",
        "My freedom is my most precious possession. I'll never let anyone take it from me again.",
        "I hold no greater cause than my service to my people.",
        "The gods of my people are a comfort to me so far from home.",
        "So long as I have this token from my homeland, I can face any adversity in this strange land.",
        "I begin or end my day with small traditional rituals that are unfamiliar to those around me.",
        "I honor my deities through practices that are foreign to this land.",
        "I express affection or contempt in ways that are unfamiliar to others.",
        "I have a strong code of honor or sense of propriety that others don't comprehend.",
        "I have my own ideas about what is and is not food, and I find the eating habits of those around me fascinating, confusing, or revolting.",
        "I have different assumptions from those around me concerning personal space, blithely invading others' space in innocence, or reacting to ignorant invasion of my own.",
        "I see morality entirely in black and white.",
        "I think far ahead, a detachedness often mistaken for daydreaming.",
        "I overexert myself, sometimes needing to recuperate for a day or more.",
        "I have no sense of humor. Laughing is uncomfortable and embarrassing.",
        "I never make eye contact.",
        "I always make eye contact and hold it unflinchingly.",
        "I an callous about death. It comes to us all eventually.",
        "I am ever learning how to be among others—when to stay quiet, when to laugh.",
        "I cultivate a single obscure hobby or study and eagerly discuss it at length.",
        "I think far ahead, a detachedness often mistaken for daydreaming.",
        "I sleep just as much as I need to and on an unusual schedule.",
        "I treasure a memento of a person or instance that set me upon my path.",
        "I strive to have no personality—it's easier to forget what's hardly there.",
        "I'm earnest and uncommonly direct.",
        "Despite my best efforts, I am unreliable to my friends.",
        "I have trouble keeping my true feelings hidden. My sharp tongue lands me in trouble.",
        "A scandal prevents me from ever going home again. That kind of trouble seems to follow me around.",
        "I'm a sucker for a pretty face.",
        "I'll do anything to win fame and renown.",
        "I idolize a hero of the old tales and measure my deeds against that person's.",
        "I change my mood or my mind as quickly as I change key in a song.",
        "I'll settle for nothing less than perfection.",
        "I get bitter if I'm not the center of attention.",
        "I love a good insult, even one directed at me.",
        "Nobody stays angry at me or around me for long, since I can defuse any amount of tension.",
        "I'm a hopeless romantic, always searching for that 'special someone.'",
        "Whenever I come to a new place, I collect local rumors and spread gossip.",
        "I know a story relevant to almost every situation.",
        "An innocent person is in prison for a crime that I committed. I'm okay with that.",
        "I turn tail and run when things look bad.",
        "I have a 'tell' that reveals when I'm lying.",
        "If there's a plan, I'll forget it. If I don't forget it, I'll ignore it.",
        "When faced with a choice between money and my friends, I usually choose the money.",
        "When I see something valuable, I can't think about anything but how to steal it.",
        "I blow up at the slightest insult.",
        "The best way to get me to do something is to tell me I can't do it.",
        "I don't pay attention to the risks in a situation. Never tell me the odds.",
        "I am incredibly slow to trust. Those who seem the fairest often have the most to hide.",
        "I would rather make a new friend than a new enemy.",
        "The first thing I do in a new place is note the locations of everything valuable – or where such things could be hidden.",
        "I am always calm, no matter what the situation. I never raise my voice or let my emotions control me.",
        "I always have a plan for what to do when things go wrong.",
        "I hate to admit it and will hate myself for it, but I'll run and preserve my own hide if the going gets tough.",
        "I can't resist swindling people who are more powerful than me.",
        "I'm too greedy for my own good. I can't resist taking a risk if there's money involved.",
        "I'm convinced that no one could ever fool me the way I fool others.",
        "I'm always in debt. I spend my ill-gotten gains on decadent luxuries faster than I bring them in.",
        "I can't resist a pretty face.",
        "I pocket anything I see that might have some value.",
        "I keep multiple holy symbols on me and invoke whatever deity might come in useful at any given moment.",
        "Sarcasm and insults are my weapons of choice.",
        "I lie about almost everything, even when there's no good reason to.",
        "I'm a born gambler who can't resist taking a risk for a potential payoff.",
        "Flattery is my preferred trick for getting what I want.",
        "I have a joke for every occasion, especially occasions where humor is inappropriate.",
        "I fall in and out of love easily, and am always pursuing someone.",
        "I convince people that worthless junk is worth their hard-earned money.",
        "I run sleight-of-hand cons on street corners.",
        "I put on new identities like clothes.",
        "I insinuate myself into people's lives to secure their fortunes.",
        "I shave coins or forge documents.",
        "I cheat at games of chance.",
        "I must be the captain of any group I join.",
        "Any defeat or failure on my part is because my opponents cheated.",
        "I have lingering pain of old injuries.",
        "I ignore anyone who doesn't compete and anyone who loses to me.",
        "I'll do absolutely anything to win.",
        "I indulge in a habit that threatens my reputation or health.",
        "I strive to live up to a specific hero's example.",
        "The person who trained me is the most important person in my world.",
        "My teammates are my family.",
        "I get irritated if people praise someone else and not me.",
        "Anything worth doing is worth doing best.",
        "I love to trade banter and gibes.",
        "When I see others struggling, I offer to help.",
        "Obstacles exist to be overcome.",
        "I have a daily exercise routine I refuse to break.",
        "I don't like to sit idle.",
        "I feel most at peace during physical exertion, whether exercise or battle.",
        "I can't sleep except in total darkness.",
        "When given the choice of going left or right, I always go left.",
        "I have no time for friends or family. I spend every waking moment thinking about and preparing for my next expedition.",
        "When I'm not exploring dungeons or ruins, I get jittery and impatient.",
        "I can't leave a room without searching it for secret doors.",
        "I have a secret fear of some common wild animal – and in my work, I see them everywhere.",
        "You might think I'm a scholar, but I love a good brawl. These fists were made for punching.",
        "I might fail, but I will never give up.",
        "I have no qualms about stealing from the dead.",
        "I love a good puzzle or mystery.",
        "I'm a pack rat who never throws anything away.",
        "I wear a tribal mask and never take it off.",
        "I complain about everything.",
        "I've picked up some unpleasant habits living among races such as goblins, lizardfolk, or orcs.",
        "I believe that I'm intellectually superior to people from other cultures and have much to teach them.",
        "Boats make me seasick.",
        "I talk to myself, and I don't make friends easily.",
        "When I arrive at a new settlement for the first time, I must learn all its customs.",
        "I would risk life and limb to discover a new culture or unravel the secrets of a dead one.",
        "By living among violent people, I have become desensitized to violence.",
        "I would rather observe than meddle.",
        "I prefer the company of those who aren't like me, including people of other races.",
        "I'm a stickler when it comes to observing proper etiquette and local customs.",
        "I judge others harshly, and myself even more severely.",
        "I put too much trust in those who wield power within my temple's hierarchy.",
        "My piety sometimes leads me to blindly trust those that profess faith in my god.",
        "I am inflexible in my thinking.",
        "I am suspicious of strangers and expect the worst of them.",
        "Once I pick a goal, I become obsessed with it to the detriment of everything else in my life.",
        "Adaptable: Shows flexibility and versatility regardless of the situation. Thinks quickly.",
        "Since no one else is stepping up, I will.",
        "Adventurous. Willing to try new experiences and take risks.",
        "Affectionate: Shows open fondness for others",
        "Compassionate. Will prevent damage to others. ",
        "In Alert. Aware of and watchful for possible change or danger.",
        "I plan ahead. Always having an exit strategy",
        "I am highly observant",
        "I am ambitious.",
        "I am confident and prideful",
        "I am analytical, logical, rational.",
        "I am highly curious.",
        "I fear making a mistake.",
        "I am bold and intrepid.",
        "I desire to prove myself",
        "I am driven by a strong sense of righteousness: The belief in a higher power or purpose",
        "I am calmed, and inclined toward tranquility and serenity",
        "I have a higher purpose.",
        "I have a boring personality.",
        "I enjoy simple pleasures",
        "I am cautious, given to prudent forethought before acting.",
        "They are wise.",
        "They are charming",
        "They are confident, fully assured of themself",
        "I am cooperative.",
        "They are courageous.",
        "They are courteous, friendly, and have good maners.",
        "They are curious. Marked by the desire to investigate and learn",
        "They have the ability to make quick, efficient decisions; lacking hesitation.",
        "They are diplomatic: Skilled at handling people while respecting their needs",
        "They are disciplined: Exhibiting willpower and self-control.",
        "They are strongly dedicated to a goal or belief",
        "They are Carefree and relaxed.",
        "They are enthusiastic: Frequently feeling or exhibiting much excitement.",
        "They are generous, altruistic, philanthropic.",
        "They are harsh, brusque, and violent.",
        "They are honorable, having noble principles and displaying integrity.",
        "They are passionate, capable of or expressing deep feeling.",
        "They are patient. Exhibiting self-control and composure under trial or strain.",
        "They are patriotic. Having love for or loyalty to their country.",
        "They are persistent: Stubbornly continuing on despite opposition, difficulty, or danger.",
        "They are playful, immature, and cheerful.",
        "They are protective.",
        "Traps don't make me nervous. Idiots who trigger traps make me nervous.",
        "I'm happier in a dusty old tomb than I am in the centers of civilization.",
        "Fame is more important to me than money.",
        "I pursue wealth to secure someone's love.",
        "I'll do anything to get my hands on something rare or priceless.",
        "I'm quick to assume that someone is trying to cheat me.",
        "I'm never satisfied with what I have – I always want more.",
        "I would kill to acquire a noble title.",
        "My kind are my family. I would do anything for them.",
        "I hide scraps of food and trinkets away in my pockets.",
        "I ask a lot of questions.",
        "I like to squeeze into small places where no one else can get to me.",
        "I sleep with my back to a wall or tree, with everything I own wrapped in a bundle in my arms.",
        "I eat like a pig and have bad manners.",
        "I think anyone who's nice to me is hiding evil intent.",
        "I don't like to bathe.",
        "I bluntly say what other people are hinting at or hiding.",
        "I am no common criminal; I am a mastermind.",
        "My friends know they can rely on me, no matter what.",
        "I work hard so that I can play hard when the work is done.",
        "I enjoy sailing into new ports and making new friends over a flagon of ale.",
        "I stretch the truth for the sake of a good story.",
        "To me, a tavern brawl is a nice way to get to know a new city.",
        "I never pass up a friendly wager.",
        "My language is as foul as a stable.",
        "I like a job well done, especially if I can convince someone else to do it.",
        "It is my duty to protect my students.",
        "An injury to the unspoiled wilderness of my home is an injury to me.",
        "My kind (family, clan, or tribe) is the most important thing in my life, even when they are far from me.",
        ""
    ]

    if background == "Expert":
        Traits += [
            "I'm horribly jealous of anyone who can outshine my handiwork. Everywhere I go, I'm surrounded by rivals.",
            "No one must ever learn that I once stole money from guild coffers.",
            "One day I will return to my guild and prove that I am the greatest artisan of them all.",
            "The workshop where I learned my trade is the most important place in the world to me.",
            "I created a great work for someone, and then found them unworthy to receive it. I'm still looking for someone worthy.",
            "I owe my guild a great debt for forging me into the person I am today.",
            "I will get revenge on the evil forces that destroyed my place of business and ruined my livelihood.",
            "I get frustrated to the point of distraction by shoddy craftsmanship.",
            "Though I am an excellent crafter, my work tends to look as though it belongs on a ship.",
            "I am so obsessed with sketching my ideas for elaborate inventions that I sometimes forget little thing like eating and sleeping.",
            "I'm judgmental of those who are not skilled with tools of some kind.",
            "I sometimes take things that don't belong to me, especially if they are very well made."
        ]

    if background == "Priest" or background == "Cultist":
        Traits += [
            "I was partaking of communal living in accordance with the dictates of a religious order.",
            "They idolize a particular hero of my faith, and constantly refer to that person's deeds and example.",
            "I can find common ground between the fiercest enemies, empathizing with them and always working toward peace.",
            "I see omens in every event and action. The gods try to speak to us, we just need to listen.",
            "Nothing can shake my optimistic attitude.",
            "I quote (or misquote) sacred texts and proverbs in almost every situation.",
            "I am tolerant  of other faiths and respect the worship of other gods.",
            "I am intolerant of other faiths and condemn the worship of other gods.",
            "I've enjoyed fine food, drink, and high society among my temple's elite. Rough living grates on me.",
            "I've spent so long in the temple that I have little practical experience dealing with people in the outside world.",
            "Nothing is more important than the other members of my hermitage, order, or association.",
            ""]
    if background == "Bard":
        Traits += [
            "My instrument is my most treasured possession, and it reminds me of someone I love."
        ]
    result = ""
    result += f"\n{random.choice(Traits)}"
    result += f"\n{random.choice(Traits)}"
    result += "\n"  
    return result


def Ideal(npc):

    background = npc.background
    alignment= npc.alignment
    
    if background == "Noble":
        if ("Good" in alignment) and Dice() == 1:
            return random.choice([
                "Noble Obligation. It is my duty to protect and care for the people beneath me.",
                "Respect. Respect is due to me because of my position, but all people regardless of station deserve to be treated with dignity."
            ])

    if background == "Priest":
        if "Lawful" in alignment and Dice() == 1:
            return random.choice([
                "Tradition. The ancient traditions of worship and sacrifice must be preserved and upheld.",
                "Faith. I trust that my deity will guide my actions. I have faith that if I work hard, things will go well."
            ])
        if "Good" in alignment and Dice() == 1:
            return random.choice(
                ["Charity. I always try to help those in need, no matter what the personal cost."
                 ])
        if "Chaotic" in alignment and Dice() == 1:
            return random.choice([
                "Change. We must help bring about the changes the gods are constantly working in the world."
            ])

    if background == "Charlatan":
        if "Chaotic" in alignment and Dice() == 1:
            return random.choice([
                "Independence. I am a free spirit – no one tells me what to do.",
                "Creativity. I never run the same con twice."
            ])
        if "Lawful" in alignment and Dice() == 1:
            return random.choice([
                "Fairness. I never target people who can't afford to lose a few coins."
            ])
        if "Good" in alignment and Dice() == 1:
            return random.choice([
                "Fairness. I never target people who can't afford to lose a few coins.",
                "Charity. I distribute the money I acquire to the people who really need it.",
                "Friendship. Material goods come and go. Bonds of friendship last forever."
            ])

    if background == "Commoner":
        if "Good" in alignment and Dice() == 1:
            return random.choice([
                "Camaraderie. Good people make even the longest voyage bearable."
            ])
        if "Lawful" in alignment and Dice() == 1:
            return random.choice([
                "Luck. Our luck depends on respecting its rules—now throw this salt over your shoulder."
            ])
        if "Chaotic" in alignment and Dice() == 1:
            return random.choice([
                "Daring. The richest bounty goes to those who risk everything."
            ])
        if "Neutral" in alignment and Dice() == 1:
            return random.choice([
                "Balance. Do not fish the same spot twice in a row; suppress your greed, and nature will reward you."
            ])

    if background == "Criminal" or background == "Bandit":
        if "Lawful" in alignment and Dice() == 1:
            return random.choice([
                "Honor. I don't steal from others in the trade.",
            ])
        if "Chaotic" in alignment and Dice() == 1:
            return random.choice([
                "Freedom. Chains are meant to be broken, as are those who would forge them.",
            ])
        if "Good" in alignment and Dice() == 1:
            return random.choice([
                "Charity. I steal from the wealthy so that I can help people in need.",
                "Redemption. There's a spark of good in everyone",
            ])
        if "Evil" in alignment and Dice() == 1:
            return random.choice([
                "Greed. I will do whatever it takes to become wealthy.",
                "Plunder. Take all that you can and leave nothing for the scavengers.",
            ])
        if "Neutral" in alignment and Dice() == 1:
            return random.choice([
                "People. I'm loyal to my friends, not to any ideals, and everyone else can take a trip down the Styx for all I care."
            ])


    if background == "Pirate":
        if "Good" in alignment and Dice() == 1:
            return random.choice([
                "Crew. If everyone on deck pitches in, we'll never sink.",
                "Respect. The thing that keeps a ship together is mutual respect between captain and crew."
            ])
        if "Lawful" in alignment and Dice() == 1:
            return random.choice([
                "Careful Lines. A ship must be balanced according to the laws of the universe.",
                "Fairness. We all do the work, so we all share in the rewards."
            ])
        if "Chaotic" in alignment and Dice() == 1:
            return random.choice([
                "Freedom. The sea is freedom-the freedom to go anywhere and do anything."
            ])
        if "Evil" in alignment and Dice() == 1:
            return random.choice([
                "Mastery. I'm a predator, and the other ships on the sea are my prey."
            ])
        if "Neutral" in alignment and Dice() == 1:
            return random.choice([
                "People. I'm committed to my crewmates, not to ideals. "
            ])
        if Dice() == 1:
            return random.choice([
                "Aspiration. Someday I'll own my own ship and chart my own destiny."
            ])

    if background == "Scholar":
        if "Lawful" in alignment and Dice() == 1:
            return random.choice(
                ["Distance. One must not interfere with the affairs of another culture – even one in need of aid.",
                 "Power. Common people crave strong leadership, and I do my utmost to provide it.",
                 "Dignity. The dead and their belongings deserve to be treated with respect."
                 ])
        if "Good" in alignment and Dice() == 1:
            return random.choice([
                "Protection. I must do everything possible to save a society facing extinction.",
                "Preservation. That artifact belongs in a museum."
            ])
        if "Evil" in alignment and Dice() == 1:
            return random.choice([
                "Indifferent. Life is cruel. What's the point in saving people if they're going to die anyway?"
            ])
        if "Chaotic" in alignment and Dice() == 1:
            return random.choice([
                "Death Wish. Nothing is more exhilarating than a narrow escape from the jaws of death."
            ])

    if background == "Bard":
        if "Good" in alignment and Dice() == 1:
            return random.choice([
                "Beauty. When I perform, I make the world better than it was."
            ])
        if "Lawful" in alignment and Dice() == 1:
            return random.choice([
                "Tradition. The stories, legends, and songs of the past must never be forgotten, for they teach us who we are."
            ])
        if "Chaotic" in alignment and Dice() == 1:
            return random.choice([
                "Creativity. The world is in need of new ideas and bold action.",
                "Invention. Make what you need out of whatever is at hand. "
            ])
        if "Evil" in alignment and Dice() == 1:
            return random.choice([
                "Greed. I'm only in it for the money and fame.",
                "Perfection. To measure a being and find it lacking is the greatest disappointment",
            ])
        if "Neutral" in alignment and Dice() == 1:
            return random.choice([
                "People. I like seeing the smiles on people's faces when I perform. That's all that matters."
            ])
        if Dice() == 1:
            return random.choice([
                "Honesty. Art should reflect the soul; it should come from within and reveal who we really are."
            ])

    if background == "Traveler":
        if "Good" in alignment and Dice() == 1:
            return random.choice([
                "Open. I have much to learn from the kindly folk I meet along my way."
            ])
        if "Lawful" in alignment and Dice() == 1:
            return random.choice([
                "Reserved. As someone new to these strange lands, I am cautious and respectful in my dealings."
            ])
        if "Chaotic" in alignment and Dice() == 1:
            return random.choice([
                "Wanderlust. I prefer to take the less traveled path",
                "Adventure. I'm far from home, and everything is strange and wonderful!"
            ])
        if "Evil" in alignment and Dice() == 1:
            return random.choice([
                " Cunning. Though I may not know their ways, neither do they know mine, which can be to my advantage."
            ])
        if "Neutral" in alignment and Dice() == 1:
            return random.choice([
                "Inquisitive. Everything is new, but I have a thirst to learn."
            ])

    if background == "Criminal":
        if "Lawful" in alignment and Dice() == 1:
            return random.choice([
                "Smuggler's Code I uphold the unwritten rules of the smugglers, who do not cheat one another or directly harm innocents."
            ])
        if "Good" in alignment and Dice() == 1:
            return random.choice([
                "Peace and Prosperity I smuggle only to achieve a greater goal that benefits my community."
            ])
        
    if background == "Warrior":
        if "Chaotic" in alignment and Dice() == 1:
            return random.choice([
                "Competition. I strive to test myself in all things."
            ])
        if "Evil" in alignment and Dice() == 1:
            return random.choice([
                "Triumph. The best part of winning is seeing my rivals brought low."
            ])
        if "Good" in alignment and Dice() == 1:
            return random.choice([
                "Camaraderie. The strongest bonds are forged through struggle."
            ])
        if "Neutral" in alignment and Dice() == 1:
            return random.choice([
                "People. I strive to inspire my spectators."
            ])
        if "Lawful" in alignment and Dice() == 1:
            return random.choice([
                "Tradition. Every game has rules, and the playing field must be level."
            ])

    if "Good" in alignment and Dice() == 1:
        return random.choice([
            "Teamwork. Success depends on cooperation and communication.",
            "Greater Good. Our lot is to lay down our lives in defense of others.",
            "Common Good. My organization serves a vital function, and its prosperity will help everyone.",
            "Greater Good. My gifts are meant to be shared with all, not used for my own benefit.",
            "Greater Good. I kill monsters to make the world a safer place, and to exorcise my own demons.",
            "Selflessness. I try to help those in need, no matter what the personal cost.",
            "Generosity. My talents were given to me so that I could use them to benefit the world.",
            "Empathy. No creature should be made to suffer.",
            "Respect. People deserve to be treated with dignity and respect.",
            "Friendship. I never leave a friend behind. ",
            "Respect. All people, rich or poor, deserve respect.",
            "Beauty. What is beautiful points us beyond itself toward what is true.",
            "Greater Good. It is each person's responsibility to make the most happiness for the whole tribe.",
        ])
    if "Chaotic" in alignment and Dice() == 1:
        return random.choice([
            "Embracing. Life is messy. Throwing yourself into the worst of it is necessary to get the job done.",
            "Independence. I must prove that I can handle myself without the coddling of my family.",
            "Change. Life is like the seasons, in constant change, and we must change with it.",
            "No Limits. Nothing should fetter the infinite possibility inherent in all existence.",
            "Independence. When people follow orders blindly, they embrace a kind of tyranny",
            "Innovation. Abandon old traditions and find better ways to do things.",
            "Free Thinking. Inquiry and curiosity are the pillars of progress.",
            "Freedom. I have a dark calling that puts me above the law.",
            "Freedom. Everyone should be free to pursue his or her own livelihood.",
            "Freedom. Tyrants must not be allowed to oppress the people.",
            "Changeability. Change is good, which is why I live by an ever-changing set of rules.",
            "Change. The low are lifted up, and the high and mighty are brought down. Change is the nature of things."
        ])
    if "Lawful" in alignment and Dice() == 1:
        return random.choice([
            "Code. The code provides a solution for every problem, and following it is imperative.",
            "Responsibility. It is my duty to respect the authority of those above me, just as those below me must respect mine.",
            "Honor. If I dishonor myself, I dishonor my whole kind.",
            "Logic. Emotions must not cloud our logical thinking.",
            "Responsibility. I do what I must and obey just authority.",
            "Tradition. I uphold traditions of my kind and bring honor to my family.",
            "Logic. Emotions must not cloud our sense of what is right and true, or our logical thinking.",
            "Logic. I like to know my enemy’s capabilities and weaknesses before rushing into battle.",
            "Community. It is the duty of all civilized people to strengthen the bonds of community and the security of civilization.",
            "Fairness. No one should get preferential treatment before the law, and no one is above the law.",
            "Honor. A deal is a deal, and I would never break one.",
            "Community. We have to take care of each other, because no one else is going to do it."
        ])
    if "Evil" in alignment and Dice() == 1:
        return random.choice([
            "Might. The strong train so that they might rule those who are weak.",
            "Power. If I can attain more power, no one will tell me what to do.",
            "Power. Knowledge is the path to power and domination.",
            "All for a Coin. I'll do nearly anything if it means I turn a profit.",
            "Might. In life as in war, the stronger force wins.",
            "Power. I want to ensure the prosperity of my kind and wield its power myself.",
            "Destruction. I’m a monster that destroys other monsters, and anything else that gets in my way.",
            "Greed. I'm only in it for the money.",
            "Might. If I become strong, I can take what I want – what I deserve.",
            "Obsession. I won't let go of a grudge",
            "Greed. I will do whatever it takes to get what I want, regardless of the harm it might cause.",
            "Confusion. Deception is a weapon. Strike from where your foes won't expect.",
            "Retribution. The rich need to be shown what life and death are like in the gutters.",
            "Might. The strongest are meant to rule.",
            "Greed. The gods make people constantly, but only made a certain quantity of gold.",
            "Power. The gods show me their favour by allowing my success and power. If they favoured others, they wouldn't be in suffering. It's theis own fault for not gaining their favour."
        ])
    if "Neutral" in alignment and Dice() == 1:
        return random.choice([
            "People. I help the people who help me-that's what keeps us alive.",
            "People. I'm committed to the people I care about, not to ideals.",
            "Danger. With every great discovery comes grave danger. The two walk hand in hand.",
            "Sincerity. There's no good in pretending to be something I'm not.",
            "Live and Let Live. Ideals aren't worth killing over or going to war for.",
            "Nature. The natural world is more important than all the constructs of civilization."
        ])
    return random.choice([
        "Perseverance. No injury or obstacle can turn me from my goal.",
        "Bravery. To act when others quake in fear- this is the essence of the warrior.",
        "Family. Blood runs thicker than water.",
        "Glory. I must earn glory in battle, for myself and my clan.",
        "Self-Improvement. The goal of a life of study is the betterment of oneself.",
        "Knowledge. The path to power and self-improvement is through knowledge.",
        "Hope. The horizon at sea holds the greatest promise.",
        "Reflection. Muddied water always clears in time.",
        "Daring. I am most happy when risking everything.",
        "People. For all my many lies, I place a high value on friendship.",
        "Wealth. Heaps of coins in a secure vault is all I dream of.",
        "Nation. My city is all that matter.",
        "Nation. My nation, is all that matter.",
        "Nation. My people are all that matter.",
        "Aspiration. I'm going to prove that I'm worthy of a better life.",
        "Comfort. I want to ensure that me and mine enjoy the best things in life.",
        "Discovery. I want to learn all I can, both for my organization and for my own curiosity.",
        "Self-Knowledge. If you know yourself, there's nothing left to know.",
        "Live and Let Live. Meddling in the affairs of others only causes trouble.",
        "Power. Solitude and contemplation are paths toward mystical power.",
        "Power. Solitude and contemplation are paths toward magical power.",
        "Determination. I’ll stop the spirits that haunt me or die trying.",
        "Aspiration. I work hard to be the best there is at my craft.",
        "Suspicious. I must be careful, for I have no way of telling friend from foe here.",
        "Destiny. Nothing and no one can steer me away from my higher calling.",
        "Anonymity. It's my deeds that should be remembered, not their instrument.",
        "Incorruptibility. Be a symbol, and leave your flawed being behind.",
        "Infamy. My name will be a malediction, a curse that fulfills my will.",
        "Security. Doing what must be done can't bring the innocent to harm.",
        "Justice. Place in society shouldn't determine one's access to what is right. ",
        "Discovery. I want to be the first person to discover a lost culture.",
        "Knowledge. By understanding other races and cultures, we learn to understand ourselves.",
        "Immortality. All my exploring is part of a plan to find the secret of everlasting life.",
        "Aspiration. I seek to prove myself worthy of my deity's favor by matching my actions against their teachings.",
        "Greed. I won't risk my life for nothing. I expect some kind of payment.",
        "Growth. Lessons hide in victory and defeat",
        "Aspiration. I'm determined to make something of myself.",
        "Hard Work. No sea can beat me if I fight hard.",
        ""
    ])
