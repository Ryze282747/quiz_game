const withdraw_btn = document.getElementById("withdraw-btn");
const balance_display = document.getElementById("balance");
let balance;

const set_balance = async () => {
  const res = await fetch("/user/balance");
  
  if (!res.ok) {
    alert(`Error status code ${res.status}`);
    window.location.href = "/logout";
  }
  
  const data = await res.json();
  
  balance = data["balance"];
  balance_display.textContent = `₱${balance.toFixed(2)}`;
}

const init = async () => {
  await set_user();
  await set_balance();
  withdraw_btn.addEventListener("click", () => {
    alert(balance);
  });
}

window.onload = init;