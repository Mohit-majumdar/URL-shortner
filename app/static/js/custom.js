async function get_short_url(url) {
  try {
    document.getElementById("loading").style.display = "block";
    csrf_token = getCookie("csrftoken");
    res = await fetch("http://127.0.0.1:8000/create_short_url", {
      method: "post",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrf_token, // Include the CSRF token in the headers
      },
      body: JSON.stringify({ orignal_url: url }),
    });
    data = await res.json();
    document.getElementById("message").textContent = data.message;

    const s_el = document.getElementById("shorturl");
    s_el.firstChild?.remove();
    el = document.createElement("a");
    el.href = data.short_url;
    el.textContent = data.short_url;
    el.target = "_blank";

    document.getElementById("shorturl").appendChild(el);
  } catch (error) {
    document.getElementById("message").textContent = `Gor error ${error}`;
  } finally {
    document.getElementById("loading").style.display = "none";
  }
}

function getCookie(name) {
  const cookieValue = document.cookie.match(
    "(^|;)\\s*" + name + "\\s*=\\s*([^;]+)"
  );
  return cookieValue ? cookieValue.pop() : "";
}

async function get_click_details(id) {
  try {
    document.getElementById("loading").style.display = "block";
    document.getElementById("details").style.display = "none";


    csrf_token = getCookie("csrftoken");
    res = await fetch("http://127.0.0.1:8000/get_details", {
      method: "post",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrf_token,
      },
      body: JSON.stringify({ id: id }),
    });
    data = await res.json();

    document.getElementById("orignal_url").textContent = data.orignal_url;
    document.getElementById("short_url").textContent = data.short_url;
    document.getElementById("created").textContent = new Date( data.created);
    document.getElementById("exprie").textContent = new Date (data.exprie);

    const items = data.clicks
    const tableBody = document.querySelector("#my-table > tbody");
    tableBody.innerHTML = ''
    items.forEach((item,i) => {
      const row = tableBody.insertRow()
      const cell0 = row.insertCell(0) 
      const cell1 = row.insertCell(1)
      const cell2 = row.insertCell(2)
      const cell3 = row.insertCell(3)

      cell0.textContent = i
      cell1.textContent = data.short_url
      cell2.textContent = item.location
      cell3.textContent = new Date(item.created_at)
      
    });

  } catch (error) {
    console.error(error)
  } finally {
    document.getElementById("loading").style.display = "none";
    document.getElementById("details").style.display = "block"
    scrollToDiv()
  }
}
function scrollToDiv() {
  // Get a reference to the target div by its id
  var targetDiv = document.getElementById("details");

  // Calculate the target scroll position
  var targetPosition = targetDiv.offsetTop;

  // Scroll to the target position
  window.scrollTo({
      top: targetPosition,
      behavior: 'smooth' // Add smooth scrolling effect
  });
}