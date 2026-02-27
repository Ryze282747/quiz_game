const inputs = document.getElementsByClassName("cred-input");
const register_btn = document.getElementById("register-btn");
const next_btn = document.getElementById("next-btn");
const pwd_container = document.getElementById("pwd-container");
const info_container = document.getElementById("info-container");
const password = document.getElementById("password");
const con_password = document.getElementById("confirm-password");
const username = document.getElementById("username");
const email = document.getElementById("email");
const show_pwd = document.getElementById("show-pwd");
const show_con = document.getElementById("show-con");

const init = async () => {
  initButtons();
  initInputs();
}

const checkContent = () => {
  
  const username_val = username.value.trim();
  const email_val = email.value.trim();
  
  if (!email.checkValidity()) {
    next_btn.disabled = true;
    return null;
  }
  
  if (username_val == "" || email_val == ""){
    next_btn.disabled = true;
    return null;
  }
  
  next_btn.disabled = false;
  
}

const checkPassword = () => {
  
  const pwd = password.value.trim();
  const con = con_password.value.trim();
  
  if (pwd == "" || con == "") {
    register_btn.disabled = true;
    return null;
  }
  
  if (pwd != con) {
    register_btn.disabled = true;
    return null;
  }
  
  register_btn.disabled = false;
  
}

const initButtons = () => {
  next_btn.addEventListener("click", nextAnimation);
  show_pwd.addEventListener("click", showPwd);
  show_con.addEventListener("click", showCon);
  register_btn.addEventListener("click", signup)
}

const initInputs = () => {
  for (let i = 0; i < inputs.length; i++) {
    inputs[i].addEventListener("input", checkContent);
  }
  password.addEventListener("input", checkPassword);
  con_password.addEventListener("input", checkPassword);
}

const nextAnimation = () => {
  pwd_container.style.animationName = "intro";
  info_container.style.animationName = "outro";
  info_container.style.animationPlayState = "running";
  pwd_container.style.animationPlayState = "running";
}

const showPwd = (e)  => {
  if (e.target.textContent === "Show") {
    password.type = "text";
    e.target.textContent = "Unshow";
  } else {
    password.type = "password";
    e.target.textContent = "Show";
  }
}

const showCon = (e)  => {
  if (e.target.textContent === "Show") {
    con_password.type = "text";
    e.target.textContent = "Unshow";
  } else {
    con_password.type = "password";
    e.target.textContent = "Show";
  }
}

const signup = async () => {
  try {
    
    register_btn.disabled = true;
    
    const payload = {
      "username":username.value,
      "password":password.value,
      "email":email.value
    }
    
    const res = await fetch("/signup", {
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
    
    if (data.exist){
      alert("Email already exist.");
      window.location.href = "/signup";
      return null;
    }
    
    alert("Account created succesfully!")
    window.location.href = "/login";
    
  } catch (e) {
    console.error(`Error: ${e}`);
  }
}

window.onload = init;
