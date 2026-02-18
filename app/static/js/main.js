const toggleButton = document.getElementById('toggle-btn')
const sidebar = document.getElementById('sidebar')
let current_user;
let username;

function toggleSidebar(){
  sidebar.classList.toggle('close')
  toggleButton.classList.toggle('rotate')

  closeAllSubMenus()
}

function toggleSubMenu(button){

  if(!button.nextElementSibling.classList.contains('show')){
    closeAllSubMenus()
  }

  button.nextElementSibling.classList.toggle('show')
  button.classList.toggle('rotate')

  if(sidebar.classList.contains('close')){
    sidebar.classList.toggle('close')
    toggleButton.classList.toggle('rotate')
  }
}

function closeAllSubMenus(){
  Array.from(sidebar.getElementsByClassName('show')).forEach(ul => {
    ul.classList.remove('show')
    ul.previousElementSibling.classList.remove('rotate')
  })
}

const set_user = async () => {
  
  const res = await fetch("/get_user");
  
  if (!res.ok) {
    alert(`Error status code ${res.status}`);
    window.location.href = "/logout";
  }
  
  const data = await res.json();
  
  current_user = data["current_user"];
  username = data["username"];
  
}
