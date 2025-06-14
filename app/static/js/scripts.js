document.getElementById('regenerate-button').addEventListener('click', function() {
	window.location.reload();
	});

document.addEventListener("DOMContentLoaded", function () {
	const menuButton = document.querySelector(".fantasy-button");
	const nav = document.querySelector("nav");

	menuButton.addEventListener("click", () => {
		nav.classList.toggle("active");
		// Toggle the visibility of the dropdown menu
		});
	});

function generateNPC_Legacy() {
		// Prevent the default form submission
		event.preventDefault();

		// Collect the form data
		const formData = new FormData(document.getElementById('npc-form'));

		fetch('/generate_npc', {
    		method: 'POST',
   			body: formData
			})
		.then(response => response.text())
		.then(data => {
    		document.getElementById('npc-container').innerHTML = data;
			})
		.catch(error => console.error('Error:', error));
	}

var typingTimeout;

function generatePortrait_Legacy(event) {
    event.preventDefault();

    // Show the loading indicator
    document.getElementById('portrait-loading-indicator').style.display = 'inline';

    // Clear the existing portrait
    clearPortrait();

    // Fetch the portrait
    fetchPortrait(true); // Added a parameter to indicate direct portrait generation
}

function clearPortrait() {
    const portraitContainer = document.getElementById('portrait-container');
    portraitContainer.innerHTML = ''; // Clear any existing portrait
}

function generateStory_Legacy(event) {
    event.preventDefault();

    // Show the loading indicators
    document.getElementById('loading-indicator').style.display = 'inline';
    document.getElementById('portrait-loading-indicator').style.display = 'inline';

    document.getElementById('story-container').innerHTML = ''; // Clear existing story

    clearTimeout(typingTimeout); // Clear existing timeout

    // Fetch the portrait and the story in parallel
    fetchPortrait(true);
    fetchStory();
}


function fetchStory() {
    const apiKey = document.getElementById('api-key-input').value;
    //if (!apiKey) {
    //    alert('Please enter your OpenAI API key.');
    //    hideLoadingIndicators();
    //    return;
    //}

    const data = new FormData();
    data.append('api_key', apiKey);

    fetch('/generate_story', {
        method: 'POST',
        body: data
    })
    .then(response => response.text())
    .then(story => {
        const storyChunks = prepareStory(story);
        typeWriter(storyChunks, 0, 0, function() {
            console.log("Done writing!");
        });
    })
    .catch(error => {
        console.error('Error:', error);
    })
    .finally(() => {
        document.getElementById('loading-indicator').style.display = 'none';
    });
}

function fetchPortrait_Legacy(isDirect) {
    const apiKey = document.getElementById('api-key-input').value;
    //if (!apiKey) {
    //    alert('Please enter your OpenAI API key.');
    //    hideLoadingIndicators();
    //    return;
    //}

    const data = new FormData();
    data.append('api_key', apiKey);

    fetch('/generate_portrait', {
        method: 'POST',
        body: data
    })
    .then(response => response.json())
    .then(data => {
        if (data.portrait_url) {
            const portraitContainer = document.getElementById('portrait-container');
            // Insert the image HTML
            const imgHtml = `<img src='${data.portrait_url}' alt='NPC Portrait' class='float-right' style='max-width: 300px; height: auto; margin: 0 0 10px 10px;'>`;
            if (isDirect) {
                // If generating a portrait directly, insert the image at the top of the story container
                document.getElementById('story-container').insertAdjacentHTML('afterbegin', imgHtml);
            } else {
                // If generating a portrait as part of story generation, append the image to the portrait container
                portraitContainer.innerHTML = imgHtml;
            }
        } else {
            console.error('Error generating portrait');
        }
    })
    .catch(error => console.error('Error:', error))
    .finally(() => {
        // Make sure to hide both indicators if there are two
        document.getElementById('loading-indicator').style.display = 'none';
        document.getElementById('portrait-loading-indicator').style.display = 'none';
    });
}





function hideLoadingIndicators() {
    document.getElementById('loading-indicator').style.display = 'none';
    document.getElementById('portrait-loading-indicator').style.display = 'none';
}


function typeWriter(chunks, chunkIndex, charIndex, fnCallback) {
    const container = document.getElementById("story-container");

    if (chunkIndex < chunks.length) {
        if (chunks[chunkIndex] === "<br>") {
            container.appendChild(document.createElement('br'));
            setTimeout(function() {
                typeWriter(chunks, chunkIndex + 1, 0, fnCallback);
            }, 100);
        } else if (charIndex < chunks[chunkIndex].length) {
            var span = document.createElement('span');
            span.innerHTML = chunks[chunkIndex].charAt(charIndex);
            span.className = 'typewriter-fade';
            container.appendChild(span);

    	typingTimeout = setTimeout(function() {
                typeWriter(chunks, chunkIndex, charIndex + 1, fnCallback);
            }, 20);
        } else {
    	typingTimeout = setTimeout(function() {
                typeWriter(chunks, chunkIndex + 1, 0, fnCallback);
            }, 100);
        }
    } else if (typeof fnCallback == 'function') {
        fnCallback();
    }

}

function prepareStory(story) {
    const regex = /<br>|[^<>]+/g;
    return story.match(regex);
}


document.getElementById('npc-form').onsubmit = function() {
    // Generate a random seed
    var seed = Math.floor(Math.random() * 10000);
		// Example: Generates a number between 0 and 9999
    document.getElementById('seed-input').value = seed;
	};

// Function to generate a list of NPCs based on selected race and background
function generateList() {
    var race = document.getElementById('race-select').value || 'Random';
    const archetype = document.getElementById('archetype-select').value || 'Random';
    window.location.href = `/list/${race}/${archetype}`;
	}

// Function to add and sub level
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.number-input').forEach((element) => {
        const input = element.querySelector('input[type="number"]');
        const minus = element.querySelector('.minus');
        const plus = element.querySelector('.plus');

        minus.addEventListener('click', () => {
            const currentValue = parseInt(input.value) || 0;
            if (currentValue > parseInt(input.min)) {
                input.value = currentValue - 1;
            }
        });

        plus.addEventListener('click', () => {
            const currentValue = parseInt(input.value) || 0;
            if (!input.max || currentValue < parseInt(input.max)) {
                input.value = currentValue + 1;
            }
        });
    });
});


document.addEventListener('DOMContentLoaded', function () {
    const grid = document.querySelector('.npc-grid');

    // Adjust grid rows to create masonry effect
    const observer = new ResizeObserver(() => {
        const gridItems = grid.querySelectorAll('.npc-box, .npc-textbox');
        grid.style.gridAutoRows = 'auto'; // Base row height
        gridItems.forEach(item => {
            const rowSpan = Math.ceil(item.offsetHeight / 10); // Calculate row span
            item.style.gridRowEnd = `span ${rowSpan}`;
        });
    });

    observer.observe(grid); // Observe changes to grid content
});



function generateNPC() {
	// Prevent the default form submission
	event.preventDefault();

	// Collect the form data
	const formData = new FormData(document.getElementById('npc-form'));

	fetch('/generate_npc', {
		method: 'POST',
		body: formData
		})
	.then(response => response.text())
	.then(data => {
		document.getElementById('npc-container').innerHTML = data;
		})
	.catch(error => console.error('Error:', error));
}

var typingTimeout;

function generatePortrait(event) {
event.preventDefault();

// Show the loading indicator
document.getElementById('portrait-loading-indicator').style.display = 'inline';

// Clear the existing portrait
clearPortrait();

// Fetch the portrait
fetchPortrait(true); // Added a parameter to indicate direct portrait generation
}

function clearPortrait() {
const portraitContainer = document.getElementById('portrait-container');
portraitContainer.innerHTML = ''; // Clear any existing portrait
}

fetch('/generate_story', {
    method: 'POST',
    body: data
})
.then(response => response.text())
.then(storyText => {
    // Insert just that text
    document.getElementById('story-container').innerHTML = storyText;
});


function fetchStory() {
const apiKey = document.getElementById('api-key-input').value;
//if (!apiKey) {
//    alert('Please enter your OpenAI API key.');
//    hideLoadingIndicators();
//    return;
//}

const data = new FormData();
data.append('api_key', apiKey);

fetch('/generate_story', {
method: 'POST',
body: data
})
.then(response => response.text())
.then(story => {
const storyChunks = prepareStory(story);
typeWriter(storyChunks, 0, 0, function() {
	console.log("Done writing!");
});
})
.catch(error => {
console.error('Error:', error);
})
.finally(() => {
document.getElementById('loading-indicator').style.display = 'none';
});
}

function fetchPortrait(isDirect) {
const apiKey = document.getElementById('api-key-input').value;
//if (!apiKey) {
//    alert('Please enter your OpenAI API key.');
//    hideLoadingIndicators();
//    return;
//}

const data = new FormData();
data.append('api_key', apiKey);

fetch('/generate_portrait', {
method: 'POST',
body: data
})
.then(response => response.json())
.then(data => {
if (data.portrait_url) {
	const portraitContainer = document.getElementById('portrait-container');
	// Insert the image HTML
	const imgHtml = `<img src='${data.portrait_url}' alt='NPC Portrait' class='float-right' style='max-width: 300px; height: auto; margin: 0 0 10px 10px;'>`;
	if (isDirect) {
		// If generating a portrait directly, insert the image at the top of the story container
		document.getElementById('story-container').insertAdjacentHTML('afterbegin', imgHtml);
	} else {
		// If generating a portrait as part of story generation, append the image to the portrait container
		portraitContainer.innerHTML = imgHtml;
	}
} else {
	console.error('Error generating portrait');
}
})
.catch(error => console.error('Error:', error))
.finally(() => {
// Make sure to hide both indicators if there are two
document.getElementById('loading-indicator').style.display = 'none';
document.getElementById('portrait-loading-indicator').style.display = 'none';
});
}





function hideLoadingIndicators() {
document.getElementById('loading-indicator').style.display = 'none';
document.getElementById('portrait-loading-indicator').style.display = 'none';
}


function typeWriter(chunks, chunkIndex, charIndex, fnCallback) {
const container = document.getElementById("story-container");

if (chunkIndex < chunks.length) {
if (chunks[chunkIndex] === "<br>") {
	container.appendChild(document.createElement('br'));
	setTimeout(function() {
		typeWriter(chunks, chunkIndex + 1, 0, fnCallback);
	}, 100);
} else if (charIndex < chunks[chunkIndex].length) {
	var span = document.createElement('span');
	span.innerHTML = chunks[chunkIndex].charAt(charIndex);
	span.className = 'typewriter-fade';
	container.appendChild(span);

typingTimeout = setTimeout(function() {
		typeWriter(chunks, chunkIndex, charIndex + 1, fnCallback);
	}, 20);
} else {
typingTimeout = setTimeout(function() {
		typeWriter(chunks, chunkIndex + 1, 0, fnCallback);
	}, 100);
}
} else if (typeof fnCallback == 'function') {
fnCallback();
}

}

function prepareStory(story) {
const regex = /<br>|[^<>]+/g;
return story.match(regex);
}

function printForma() {
  // Select the element to print
  const printElement = document.getElementById("Forma");

  // Get the stylesheets from the current page
  const stylesheets = Array.from(document.styleSheets)
    .map((styleSheet) => {
      try {
        if (styleSheet.href) {
          return `<link rel="stylesheet" href="${styleSheet.href}">`;
        } else if (styleSheet.cssRules) {
          let rules = Array.from(styleSheet.cssRules)
            .map((rule) => rule.cssText)
            .join("");
          return `<style>${rules}</style>`;
        }
      } catch (e) {
        console.error("Error accessing stylesheet:", e);
        return ""; // Skip inaccessible stylesheets
      }
    })
    .join("");

  // Create a new window for printing
  const printWindow = window.open("", "_blank", "width=800,height=600");

  // Write the content of the element into the new window
  printWindow.document.write(`
    <html>
      <head>
        <title>Print NPC</title>
        ${stylesheets} <!-- Add the styles -->
      </head>
      <body>
        ${printElement.outerHTML} <!-- Add the grid element -->
      </body>
    </html>
  `);

  // Close the document to finish loading
  printWindow.document.close();

  // Wait for the new window to load, then print
  printWindow.onload = function () {
    printWindow.print();
    printWindow.close();
  };
}


document.getElementById('try-again-button').addEventListener('click', function () {
	const newSeed = Math.floor(Math.random() * 2 ** 12);
	window.location.href = `/npc/${encodeURIComponent(npcData.race)}/${encodeURIComponent(npcData.archetype)}/${encodeURIComponent(npcData.level)}/${newSeed}`;
	});


document.addEventListener('DOMContentLoaded', function () {
    // Select all anchor tags within npc-list
    var links = document.querySelectorAll('.npc-list a');

    // Iterate through each link and add event listeners
    links.forEach(function (link) {
        // Mouse over effect
        link.addEventListener('mouseover', function () {
            link.classList.add('shine');
        });

        // Mouse out effect
        link.addEventListener('mouseout', function () {
            link.classList.remove('shine');
        });
    });
});

function reloadPage() {
	location.reload();
	}
