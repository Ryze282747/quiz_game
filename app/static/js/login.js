const show_pwd_btn = document.getElementById("show-pwd-btn");
const password_field = document.getElementById("password");
const email_field = document.getElementById("email");
const login_btn = document.getElementById("login-btn");

const showPassword = (e)  => {
  if (e.target.textContent === "Show") {
    password_field.type = "text";
    e.target.textContent = "Unshow";
  } else {
    password_field.type = "password";
    e.target.textContent = "Show";
  }
}

const login = async () => {
  try {
    
    const payload = {
      "email":email_field.value.trim(),
      "password":password_field.value.trim()
    }
    
    const res = await fetch("/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(payload)
    });
    
    if (!res.ok){
      throw new Error(`Request failed. Status: ${res.status}`);
    }
    
    const data = await res.json();
    
    if (data.access) {
      window.location.href = "/";
      //setCookieinLocalStorage
    }
    
    if (!data.access){
      alert("Invalid credentials.");
      email_field.value = "";
      password_field.value = "";
    }
    
  } catch (e) {
    console.error(`Error: ${e}`);
  }
}

show_pwd_btn.addEventListener("click", showPassword);
login_btn.addEventListener("click", login);