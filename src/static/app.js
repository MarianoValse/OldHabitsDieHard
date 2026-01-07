fetch("/habitos")
  .then(res => res.json())
  .then(data => {
    const cont = document.getElementById("habitos");
    data.forEach(h => {
      const btn = document.createElement("button");
      btn.innerText = h.nombre;
      btn.style.display = "block";
      btn.style.fontSize = "20px";
      btn.style.margin = "10px";

      btn.onclick = () => {
        fetch("/registro", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ habito_id: h.id, valor: 1 })
        });
        btn.style.background = "lightgreen";
      };

      cont.appendChild(btn);
    });
  });
