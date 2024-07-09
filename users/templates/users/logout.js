const handlelogOut = () => {
    const token = localStorage.getItem("token");
  
    fetch("https://recipe-share-w2wu.onrender.com/users/logout/", {
      method: "POST",
      headers: {
        Authorization: `Token ${token}`,
        "Content-Type": "application/json",
      },
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        localStorage.removeItem("token");
        localStorage.removeItem("user_id");
      });
  };