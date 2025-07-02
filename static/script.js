document.getElementById("tokenForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const name = document.getElementById("name").value;
  const symbol = document.getElementById("symbol").value;

  const res = await fetch("/launch-token", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, symbol }),
  });

  const data = await res.json();
  document.getElementById("output").innerText = JSON.stringify(data, null, 2);
});
