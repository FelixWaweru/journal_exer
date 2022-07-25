function countChars() {
  var len = document.getElementById("journal_entry").value.length;
  document.getElementById("entry_counter").innerHTML = 500 - len;
}