// Dark Mode
darkMode(localStorage.getItem("mode"));

function switchTheme(){
  var curr_status = localStorage.getItem("mode");
  
  if(curr_status == "light"){
    localStorage.setItem("mode", "dark");
  }
  else if(curr_status == "dark") {
    localStorage.setItem("mode", "light");
  }
  else if (curr_status == null) {
    localStorage.setItem("mode", "dark");
  }

  console.log(localStorage.getItem("mode"))
  darkMode(localStorage.getItem("mode"));
}

// Dark Mode
function darkMode(status) {

  var element = document.body;
  var fields = document.getElementsByTagName('input');
  var labels = document.getElementsByTagName('label');
  var spans = document.getElementsByTagName('span');
  var lines = document.getElementsByTagName('li');
  var textinput = document.getElementsByClassName("form-control");
  var accordion_header = document.getElementsByClassName("accordion-button");
  var accordion_content = document.getElementsByClassName("accordion-body");

  if(status == "dark") {
    element.classList.toggle("dark-mode-body");

    for (let i = 0; i < fields.length; i++) {
      fields[i].classList.toggle("dark-mode-textarea");
    }

    for (let i = 0; i < labels.length; i++) {
      labels[i].classList.toggle("dark-mode-labels");
    }

    for (let i = 0; i < spans.length; i++) {
      spans[i].classList.toggle("dark-mode-labels");
    }

    for (let i = 0; i < lines.length; i++) {
      lines[i].classList.toggle("dark-mode-labels");
    }

    for (let i = 0; i < textinput.length; i++) {
      textinput[i].classList.toggle("dark-mode-textarea");
    }
    
    for (let i = 0; i < accordion_header.length; i++) {
      accordion_header[i].classList.toggle("dark-mode-accordion-header");
    }

    for (let i = 0; i < accordion_content.length; i++) {
      accordion_content[i].classList.toggle("dark-mode-accordion-content");
    }
  }

  if (status == "light") {
    element.classList.remove("dark-mode-body");

    for (let i = 0; i < fields.length; i++) {
      fields[i].classList.remove("dark-mode-textarea");
    }

    for (let i = 0; i < labels.length; i++) {
      labels[i].classList.remove("dark-mode-labels");
    }

    for (let i = 0; i < spans.length; i++) {
      spans[i].classList.remove("dark-mode-labels");
    }

    for (let i = 0; i < lines.length; i++) {
      lines[i].classList.remove("dark-mode-labels");
    }
    
    for (let i = 0; i < textinput.length; i++) {
      textinput[i].classList.remove("dark-mode-textarea");
    }

    for (let i = 0; i < accordion_header.length; i++) {
      accordion_header[i].classList.remove("dark-mode-accordion-header");
    }

    for (let i = 0; i < accordion_content.length; i++) {
      accordion_content[i].classList.remove("dark-mode-accordion-content");
    }
  }
}

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