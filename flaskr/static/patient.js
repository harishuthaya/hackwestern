function clearText(event) {
  // event.preventDefault()
  var username = getCookie('username')
  var symptoms = document.getElementById('input').value;
  var phonenumber = document.getElementById('phone').value;
  console.log("username", username)
  console.log("symptoms", symptoms)
  console.log("phonenumber", phonenumber)

  fetch('/updatinguser?username=' + encodeURIComponent(username) + '&symptoms=' + encodeURIComponent(symptoms)
  +'&phonenumber='+encodeURIComponent(phonenumber), {"method": "POST"})
      .then(response => response.json())
      .then(data => {
          console.log(data)
      })
      .catch(error => {
          console.error('Error:', error);
      });

  // Get the input element
  var inputElement = document.getElementById("input");
  var textBoxContainer = document.getElementById("text");
  var messageDisplay = document.getElementById("messageDisplay");

  // Get the value of the input
  var inputValue = inputElement.value;

  // Do something with the input value (e.g., send it to a server)

  // Clear the value of the input
  inputElement.value = "";
  textBoxContainer.value = "";

  // Display a thank you message
  messageDisplay.innerText = "Thank you. A doctor will be with you shortly.";

  // Clear the message after a short delay (e.g., 3 seconds)
  setTimeout(function () {
    messageDisplay.innerText = "";
  }, 5000);
}
function getCookie(name) {
var cookies = document.cookie.split(';');
for (var i = 0; i < cookies.length; i++) {
    var cookie = cookies[i].trim();
    if (cookie.startsWith(name + '=')) {
        return cookie.substring(name.length + 1);
    }
}
return '';
}