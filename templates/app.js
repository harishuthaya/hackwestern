// Check login status when the page loads
document.addEventListener('DOMContentLoaded', function() {
  checkLoginStatus();
});

function login() {
  var username = document.getElementById('username').value;
  var password = document.getElementById('password').value;
  
  // Simulate a login request to the backend
  // In a real application, you would make an actual HTTP request to the backend
  if (username === 'user' && password === 'pass') {
      // Set a cookie to indicate that the user is logged in
      document.cookie = 'loggedIn=true; path=/';

      // Redirect or update the UI as needed
      checkLoginStatus();
  } else {
      document.getElementById('loginError').textContent = 'Invalid username or password';
  }
}

function checkLoginStatus() {
  var isLoggedIn = getCookie('loggedIn') === 'true';

  if (isLoggedIn) {
      // User is logged in, show authenticated content or redirect to a dashboard
      document.getElementById('loginContainer').innerHTML = '<h2>Welcome, User!</h2>';
  } else {
      // User is not logged in, show the login form
      document.getElementById('loginContainer').innerHTML = `
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
