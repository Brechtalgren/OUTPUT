const API = "/api";

// Ensure axios is loaded before using it
if (typeof axios === 'undefined') {
  console.error('Axios is not loaded! Please ensure axios is loaded before this script.');
}

// Define API functions globally
window.API_UTILS = {
  fetchPosts: async () => {
    try {
      const response = await axios.get(`${API}/posts`);
      return response.data;
    } catch (error) {
      console.error('Error fetching posts:', error);
      throw error;
    }
  },
  
  addPost: async (content) => {
    try {
      const response = await axios.post(`${API}/posts`, {
        content
      });
      return response.data;
    } catch (error) {
      console.error('Error adding post:', error);
      throw error;
    }
  }
};
