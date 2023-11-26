// Check login status when the page loads
document.addEventListener('DOMContentLoaded', function() {
  // checkLoginStatus();
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

function signup(event,activeButton) {
  event.preventDefault()
  var fullname = document.getElementById('fullname').value;
  var email = document.getElementById('email').value;
  var username = document.getElementById('username').value;
  var password = document.getElementById('password').value;
  var dob = document.getElementById('dob').value;
  var button1 = document.getElementById('button1')
  doctor = 1
  if (button1 === activeButton) doctor = 0
  console.log(doctor)
  var sex = document.getElementById('sex').value;
  console.log("signup func triggered")
  fetch('/validatesignup?username=' + encodeURIComponent(username) + '&password=' + encodeURIComponent(password)
  + '&fullname=' + encodeURIComponent(fullname)+'&email=' + encodeURIComponent(email)
  + '&dob=' + encodeURIComponent(dob)+'&doctor=' + encodeURIComponent(doctor) + 
  '&sex=' + encodeURIComponent(sex), {"method": "POST"})
        .then(response => response.json())
        .then(data => {
          console.log(data.valid)
            if (data.valid === "success") {
              console.log("successsss")
                // document.getElementById('signupError').textContent = 'User account created!';
                document.cookie = `username=${username}; path=/`;
                console.log("Success")
                if (data.valid === "success") {
                  document.cookie = `username=${username}; path=/`;
                  if (doctor === 1) {
                    window.location.href = "/med/dashboard";
                  } else {
                    window.location.href = "/patient";
                  }
            }} else {
                document.getElementById('signupError').textContent = 'That username or email is already taken.';
                console.log("Fail")
            }
        })
        .catch(error => {
            console.log('Error:', error);
        });
}

// function checkLoginStatus() {
//   var isLoggedIn = getCookie('loggedIn') === 'true';

//   if (isLoggedIn) {
//       // User is logged in, show authenticated content or redirect to a dashboard
//       console.log("here")
//       document.getElementById('signup-container').innerHTML = '<h2>Welcome, User!</h2>';
//   } else {
//     //   User is not logged in, show the login form
//       document.getElementById('signup-container').innerHTML = `
//       <h2>Sign Up</h2>
//       <form id="signupForm">
//           <div class="form-group">
//               <label for="username">Username:</label>
//               <input type="text" id="username" name="username" required>
//           </div>
//           <div class="form-group">
//               <label for="password">Password:</label>
//               <input type="password" id="password" name="password" required>
//           </div>
//           <div class="form-group">
//               <label for="name">Name:</label>
//               <input type="text" id="name" name="name" required>
//           </div>
//           <div class="form-group">
//               <label for="phone">Phone Number:</label>
//               <input type="tel" id="phone" name="phone" required>
//           </div>
//           <div class="form-group">
//               <label for="dob">Date of Birth:</label>
//               <input type="date" id="dob" name="dob" required>
//           </div>
//           <div class="form-group">
//               <label for="gender">Gender:</label>
//               <select id="gender" name="gender" required>
//                   <option value="male">Male</option>
//                   <option value="female">Female</option>
//                   <option value="other">Other</option>
//               </select>
//           </div>
//           <div class="form-group">
//               <button type="submit" onclick="signup(event)">Sign Up</button>
//           </div>
//           <div class="form-group">
//               <p  id="signupError" class="error-message"></p>
//           </div>
//       </form>
//       `;
//   }
// }

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