document.querySelector("form").addEventListener("submit", function (event) {
  event.preventDefault();

  const message = document.getElementById("message");

  // Get all input values
  const firstName = document.getElementById("firstName").value.trim();
  const lastName = document.getElementById("lastName").value.trim();
  const email = document.getElementById("email").value.trim();
  const mobile = document.getElementById("mobile").value.trim();
  const password = document.getElementById("password").value;
  const confirmPassword = document.getElementById("confirmPassword").value;

  // Start with assuming it's valid
  let isValid = true;
  let error = "";

  if (!firstName) {
    isValid = false;
    error += "First name is required. ";
  }

  if (!lastName) {
    isValid = false;
    error += "Last name is required. ";
  }

  if (!email.includes("@")) {
    isValid = false;
    error += "Please enter a valid email. ";
  }

  if (password !== confirmPassword) {
    isValid = false;
    error += "Passwords do not match. ";
  }

  // Show message
  if (isValid) {
    message.textContent = "All inputs are valid!";
    message.style.color = "green";
  } else {
    message.textContent = error;
    message.style.color = "red";
  }
});
