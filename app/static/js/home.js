const withdraw_btn = document.getElementById("withdraw-btn");
const withdraw_amount = document.getElementById("withdraw-amount");
const balance_display = document.getElementById("balance");
const points_display = document.getElementById("total-points");
const rank_display = document.getElementById("current-rank");
const earnings_display = document.getElementById("total-earnings");
let balance, points, rank, earnings;

const set_balance = async () => {
  const res = await fetch("/user/balance");
  
  if (!res.ok) {
    alert(`Error status code ${res.status}`);
    window.location.href = "/logout";
  }
  
  const data = await res.json();
  
  balance = data["balance"];
  
  if (balance > 999) {
    balance_display.textContent = `₱${balance.toLocaleString()}`;
    return;
  }
  
  balance_display.textContent = `₱${balance.toFixed(2)}`;
}

const set_points = async () => {
  const res = await fetch("/user/points");
  
  if (!res.ok) {
    alert(`Error status code ${res.status}`);
    window.location.href = "/logout";
  }
  
  const data = await res.json();
  
  points = data["points"];
  points_display.textContent = points.toLocaleString();
}

const set_rank = async () => {
  const res = await fetch("/user/rank");
  
  if (!res.ok) {
    alert(`Error status code ${res.status}`);
    window.location.href = "/logout";
  }
  
  const data = await res.json();
  
  rank = data["rank"];
  rank_display.textContent = `#${rank.toLocaleString()}`;
}

const set_earnings = async () => {
  const res = await fetch("/user/earnings");
  
  if (!res.ok) {
    alert(`Error status code ${res.status}`);
    window.location.href = "/logout";
  }
  
  const data = await res.json();
  
  earnings = data["earnings"];
  
  if (earnings > 999) {
    earnings_display.textContent = `₱${earnings.toLocaleString()}`;
    return;
  }
  
  earnings_display.textContent = `₱${earnings.toFixed(2)}`;
}

const withdraw = async () => {
  
  withdraw_btn.disabled = true;
  
  if (!withdraw_amount.checkValidity() || withdraw_amount.value < 1){
    alert("Please enter valid amount.");
    withdraw_btn.disabled = false;
    return;
  }
  
  const amount = Number(withdraw_amount.value);
  
  const payload = {
    "amount":amount
  }
  
  const res = await fetch("/user/balance/withdraw", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  });
  
  if (!res.ok) {
    alert("An error occured. Please try again.");
  }
  
  const data = await res.json();
  
  console.log(data);
  alert(data["msg"]);
  
  withdraw_btn.disabled = false;
  
  await set_balance();
  await set_earnings();
  
}

const init = async () => {
  await set_balance();
  await set_points();
  await set_rank();
  await set_earnings();
  withdraw_btn.addEventListener("click", withdraw);
}

window.onload = init;