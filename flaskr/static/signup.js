// Check login status when the page loads
document.addEventListener('DOMContentLoaded', function() {
  checkLoginStatus();
  // Redirect or update UI as needed here.
});

function login() {
  var username = document.getElementById('username').value;
  var password = document.getElementById('password').value;
  fetch('/validatelogin?username=' + encodeURIComponent(username) + '&password=' + encodeURIComponent(password), {"method": "POST"})
        .then(response => response.json())
        .then(data => {
            if (data.valid === "success") {
                document.getElementById('signupError').textContent = 'Username and password are valid!';
                document.cookie = 'loggedIn=true; path=/';
                checkLoginStatus();
            } else {
                document.getElementById('signupError').textContent = 'Invalid username or password.';
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function signup(event) {
  event.preventDefault()
  var username = document.getElementById('username').value;
  var password = document.getElementById('password').value;
  console.log("signup func triggered")
  fetch('/validatesignup?username=' + encodeURIComponent(username) + '&password=' + encodeURIComponent(password), {"method": "POST"})
        .then(response => response.json())
        .then(data => {
            if (data.valid === "success") {
                document.getElementById('signupError').textContent = 'Username and password are valid!';
                document.cookie = 'loggedIn=true; path=/';
                console.log("Success")
                checkLoginStatus();
            } else {
                document.getElementById('signupError').textContent = 'That username is already taken.';
                console.log("Fail")
            }
        })
        .catch(error => {
            console.log('Error:', error);
        });
}

function checkLoginStatus() {
  var isLoggedIn = getCookie('loggedIn') === 'true';

  if (isLoggedIn) {
      // User is logged in, show authenticated content or redirect to a dashboard
      console.log("here")
      document.getElementById('signup-container').innerHTML = '<h2>Welcome, User!</h2>';
  } else {
    //   User is not logged in, show the login form
      document.getElementById('signup-container').innerHTML = `
      <h2>Sign Up</h2>
      <form id="signupForm">
          <div class="form-group">
              <label for="username">Username:</label>
              <input type="text" id="username" name="username" required>
          </div>
          <div class="form-group">
              <label for="password">Password:</label>
              <input type="password" id="password" name="password" required>
          </div>
          <div class="form-group">
              <label for="name">Name:</label>
              <input type="text" id="name" name="name" required>
          </div>
          <div class="form-group">
              <label for="phone">Phone Number:</label>
              <input type="tel" id="phone" name="phone" required>
          </div>
          <div class="form-group">
              <label for="dob">Date of Birth:</label>
              <input type="date" id="dob" name="dob" required>
          </div>
          <div class="form-group">
              <label for="gender">Gender:</label>
              <select id="gender" name="gender" required>
                  <option value="male">Male</option>
                  <option value="female">Female</option>
                  <option value="other">Other</option>
              </select>
          </div>
          <div class="form-group">
              <button type="submit" onclick="signup(event)">Sign Up</button>
          </div>
          <div class="form-group">
              <p  id="signupError" class="error-message"></p>
          </div>
      </form>
      `;
  }
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
