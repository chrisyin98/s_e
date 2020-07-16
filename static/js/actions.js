"use strict";

function getResults() {
  const entry = document.getElementById('search-bar').value;
  const url = window.origin;
  console.log(entry);
  console.log(url);
  fetch(url + '/search', {
    method: "POST",
    body: JSON.stringify(entry)
  })
}

