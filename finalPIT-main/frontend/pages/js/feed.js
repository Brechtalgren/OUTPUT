// Wait for the DOM to be fully loaded
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeApp);
} else {
  initializeApp();
}

function initializeApp() {
  // Check if axios and API utilities are available
  if (typeof axios === 'undefined') {
    console.error('Axios is not loaded!');
    return;
  }
  
  if (typeof window.API_UTILS === 'undefined') {
    console.error('API_UTILS is not loaded!');
    return;
  }
  
  const feed = document.getElementById("feed");
  
  const render = ({ user, content, created_at }) => {
    const card = document.createElement("div");
    card.className = "card";
    card.innerHTML = `
      <strong>@${user}</strong>
      <p>${content}</p>
      <small>${new Date(created_at).toLocaleString()}</small>
    `;
    feed.appendChild(card);
  };
  
  (async () => {
    try {
      const posts = await window.API_UTILS.fetchPosts();
      posts.forEach(render);
    } catch (error) {
      console.error('Failed to load posts:', error);
      if (feed) {
        feed.innerHTML = '<div class="card">Failed to load posts. Please try again later.</div>';
      }
    }
  })();
}
