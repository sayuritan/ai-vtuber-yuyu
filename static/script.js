// static/script.js
const chat = document.getElementById("chat");
const input = document.getElementById("input");
const sendBtn = document.getElementById("send");

const ws = new WebSocket(`ws://${location.host}/ws/chat`);

ws.onmessage = (event) => {
  const msg = document.createElement("div");
  msg.className = "message bot";
  msg.textContent = event.data;
  chat.appendChild(msg);
  chat.scrollTop = chat.scrollHeight;
};

sendBtn.onclick = () => {
  const text = input.value;
  if (!text) return;
  const msg = document.createElement("div");
  msg.className = "message user";
  msg.textContent = text;
  chat.appendChild(msg);
  ws.send(text);
  input.value = "";
};
