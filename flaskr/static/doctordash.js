// need to check cookie and make sure that the cookie says they are a doctor. 
// if couldn't verify as doctor, send to login page. 
// Check login status when the page loads
document.addEventListener('DOMContentLoaded', function() {
  // checkLoginStatus(); // Comment this out for now. 
  fetchPatients()
});

function fetchPatients() {
  fetch('/api/get/patients', {"method": "POST"})  // Replace with your actual API endpoint
      .then(response => {
          if (!response.ok) {
              throw new Error('Network response was not ok');
          }
          return response.json();
      })
      .then(data => {
        data.forEach(patient => {
          console.log(patient[0])
          console.log(patient[1])
        })
        console.log(data[0])
          populatePatientsTable(data);
      })
      .catch(error => {
          console.error('Error:', error);
      });
}

function populatePatientsTable(patients) {
  var table = document.getElementById("patientsTable");

  patients.forEach(patient => {
      var row = table.insertRow(-1);
      row.insertCell(0).innerHTML = patient[1];
      row.insertCell(1).innerHTML = patient[2];
      row.insertCell(2).innerHTML = patient[5];
      row.insertCell(3).innerHTML = patient[6];
      row.insertCell(4).innerHTML = patient[8];
      row.insertCell(5).innerHTML = patient[5];
      var connectCell = row.insertCell(6);
      connectCell.innerHTML = `<a href="javascript:void(0)" onclick="connectToVideo(${patient.id})">Connect</a>`;
  });
}

function connectToVideo() {
  fetch('/api/create/room', {"method": "POST"})
        .then(response => response.json())
        .then(data => {
            window.open("https://doctor.metered.live/"+data.roomName)
            // console.log("doctor.metered.live/" + data.roomName)
            // console.log(data.roomName)
        })
        .catch(error => {
            console.log(error);
        });
}

// Need to add validation that a real doctor is logged in.

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

// function getCookie(name) {
//   var cookies = document.cookie.split(';');
//   for (var i = 0; i < cookies.length; i++) {
//       var cookie = cookies[i].trim();
//       if (cookie.startsWith(name + '=')) {
//           return cookie.substring(name.length + 1);
//       }
//   }
//   return '';
// }
