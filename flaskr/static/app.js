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
                document.getElementById('loginError').textContent = 'Username and password are valid!';
                document.cookie = 'loggedIn=true; path=/';
                checkLoginStatus();
            } else {
                document.getElementById('loginError').textContent = 'Invalid username or password.';
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function signup() {
  var username = document.getElementById('username').value;
  var password = document.getElementById('password').value;
  fetch('/validatesignup?username=' + encodeURIComponent(username) + '&password=' + encodeURIComponent(password), {"method": "POST"})
        .then(response => response.json())
        .then(data => {
            if (data.valid === "success") {
                document.getElementById('loginError').textContent = 'Username and password are valid!';
                document.cookie = 'loggedIn=true; path=/';
                console.log("Success")
                checkLoginStatus();
            } else {
                document.getElementById('loginError').textContent = 'That username is already taken.';
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
      document.getElementById('login-container').innerHTML = '<h2>Welcome, User!</h2>';
  } else {
      // User is not logged in, show the login form
      document.getElementById('login-container').innerHTML = `
          <h2>Login</h2>
          <form id="loginForm">
              <label for="username">Username:</label>
              <input type="text" id="username" name="username" required>
              
              <label for="password">Password:</label>
              <input type="password" id="password" name="password" required>

              <button type="button" onclick="login()">Login</button>
              <p id="loginError" class="error-message"></p>
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
