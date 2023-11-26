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
      connectCell.innerHTML = `<a href="javascript:void(0)" onclick="connectToVideo(${patient[10]})">Connect</a>`;
  });
}

function connectToVideo(phone) {
  console.log(phone)
  fetch('/api/create/room?phone=' + encodeURIComponent(phone), {"method": "POST"})
        .then(response => response.json())
        .then(data => {
            window.open("https://doctor.metered.live/"+data.roomName)
            // window.open("video?roomname="+data.roomName)
            // console.log("doctor.metered.live/" + data.roomName)
            // console.log(data.roomName)
        })
        .catch(error => {
            console.log(error);
        });
}
