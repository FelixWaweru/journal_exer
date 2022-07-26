function countChars() {
  var len = document.getElementById("journal_entry").value.length;
  document.getElementById("entry_counter").innerHTML = 500 - len;
}

// Disable submit on enter key press
$(document).keypress(
  function (event) {
    if (event.which == '13') {
      event.preventDefault();
    }
  });