//Query All input fields
var form_fields = document.getElementsByTagName("input");
form_fields[1].placeholder = "Redistributor Name";
form_fields[2].placeholder = "Email";
form_fields[3].placeholder = "Username";
form_fields[4].placeholder = "Phone";
form_fields[5].placeholder = "Address";
form_fields[6].placeholder = "Password";
form_fields[7].placeholder = "Confirm Password";

for (var field in form_fields) {
  form_fields[field].className += " form-control";
}


var resName = document.getElementById('id_name_of_food_redis')
resName.placeholder = "Redistributor Name"

var email = document.getElementById('id_email')
email.placeholder = "Email"

var username = document.getElementById('id_username')
username.placeholder = "Username"

var phone = document.getElementById('id_phone')
phone.placeholder = "Phone"

var address = document.getElementById('id_address')
address.placeholder = "Address"

var password = document.getElementById('id_password1')
password.placeholder = "Password"

var confirmPassword = document.getElementById('id_password2')
confirmPassword.placeholder = "Confirm Password"