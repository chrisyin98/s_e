"use strict";
document.body.onkeydown = function(e) {
  if(e.keyCode == 13) {
    getResults();
  }
}
function getResults() {
  const entry = id('search-bar').value;
  const url = window.origin;
  console.log(entry);
  console.log(url);
  fetch(url + '/search', {
    method: "POST",
    body: entry
  }).then(resp => resp.json())
  .then(displayResults)
  .catch(handleError);
}

function displayResults(info) {
  console.log(info);
  id('s-results').innerHTML = "";
  if(info.length < 1) {
    let text = document.createElement('p');
    text.textContent = "No results found"
    id('s-results').appendChild(text);
  }
  for(let i = 0; i < info.length; i++) {
    let text = document.createElement('p');
    text.textContent = "Website: " + info[i].website_nme;
    let text2 = document.createElement('p');
    text2.textContent = "Description: " + info[i].descrip;
    id('s-results').appendChild(text);
    id('s-results').appendChild(text2);
  }

}

function handleError(err) {
  console.log(err);
}

function id(name) {
  return document.getElementById(name);
}
