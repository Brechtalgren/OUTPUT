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
  
  const btn = document.getElementById("submit");
  const text = document.getElementById("content");
  
  if (btn && text) {
    btn.onclick = async () => {
      if (!text.value.trim()) return alert("Write something!");
      
      try {
        console.log('Creating post with content:', text.value);
        await window.API_UTILS.addPost(text.value);
        console.log('Post created successfully');
        location.href = "/feed.html";
      } catch (error) {
        console.error('Failed to create post:', error);
        alert('Failed to create post. Please try again.');
      }
    };
  } else {
    console.error('Required elements not found');
  }
}
