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
                document.cookie = `username=${username}; path=/`;
                if (data.doctor[0] === true) {
                  window.location.href = "/med/dashboard";
                } else {
                  window.location.href = "/patient";
                }
            } else {
              console.log("login failed")
                document.getElementById('loginError').textContent = 'Invalid username or password.';
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function checkLoginStatus() {
  console.log("fullcookie",document.cookie)
  var isLoggedIn = getCookie('loggedIn') === 'true';
  var doctor = getCookie('doctor') === true;
  console.log(getCookie('loggedIn'))
  console.log(getCookie('doctor'))
  console.log(getCookie('username'))
  console.log("doctor:",doctor)

  if (isLoggedIn) {
      // User is logged in, show authenticated content or redirect to a dashboard
      console.log("here")
      document.getElementById('login-container').innerHTML = '<h2>Welcome, User!</h2>';
  } else {
    //   User is not logged in, show the login form
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

function getCookie(cookieName) {
  const cookieString = document.cookie;
  const cookieArray = cookieString.split(';');
  console.log("name", cookieName)
  console.log("array", cookieArray)
  

  for (let i = 0; i < cookieArray.length; i++) {
      let cookie = cookieArray[i].trim(); // Trim any leading or trailing spaces
      console.log("entries", cookie)

      if (cookie.startsWith(cookieName + '=')) {
          return cookie.substring(cookieName.length + 1);
      }
  }

  return null;
}