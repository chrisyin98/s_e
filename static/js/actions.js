"use strict";
document.body.onkeydown = function(e) {
  if(e.keyCode == 13) {
    getResults();
  }
}
function getResults() {
  const entry = id('search-bar').value;
  const url = window.origin;
  const loadingDisplay = document.createElement('p');
  loadingDisplay.textContent = "Searching.."
  loadingDisplay.style = "font-size:20px;";
  id('s-results').appendChild(loadingDisplay);
  fetch(url + '/search', {
    method: "POST",
    body: entry
  }).then(resp => resp.json())
  .then(displayResults)
  .catch(handleError);
}

function displayResults(info) {
  id('s-results').innerHTML = "";
  if(info.length < 1) {
    let text = document.createElement('p');
    text.textContent = "No results found."
    id('s-results').appendChild(text);
  }
  for(let i = 0; i < info.length; i++) {
    let web = document.createElement('p');
    web.id = 'web-name'
    web.textContent = "Website: ";
    let website = document.createElement('a');
    website.href = info[i].website_nme;
    website.textContent = info[i].website_nme;
    website.style = "font-size:20px;";
    let num = document.createElement('p');
    num.textContent = "cos_sim weight: " + info[i].weight;
    num.style = "font-size:10px;";
    let description = document.createElement('p');
    description.textContent = "Description: " + info[i].descrip;
    id('s-results').appendChild(web);
    id('s-results').appendChild(website);
    id('s-results').appendChild(num)
    id('s-results').appendChild(description);
  }

}

function handleError(err) {
  console.log(err);
}

function id(name) {
  return document.getElementById(name);
}
