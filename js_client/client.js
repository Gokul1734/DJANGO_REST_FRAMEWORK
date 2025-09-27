const loginForm = document.getElementById('login-form');
basepoint = 'http://localhost:8000/api'

if (loginForm) {
   loginForm.addEventListener('submit',handleLogin);
}

async function handleLogin(event) {
   event.preventDefault();

   const loginEndPoint = `${basepoint}/token/`;
   const loginFormData = new FormData(loginForm);
   const ObjectData = Object.fromEntries(loginFormData);

   const options = {
      method: "POST",
      headers: {
         "Content-Type": "application/json"
      },
      body: JSON.stringify(ObjectData)
   };

   try {
      const response = await fetch(loginEndPoint, options);
      if (response.ok) {
         const data = await response.json();
         console.log(data);
         localStorage.setItem('access', data.access);
      } else {
         console.error("Login failed", response.status);
      }
   } catch (err) {
      console.error("err", err);
   }
}

async function fetchProducts(event) {
   const productsEndPoint = `${basepoint}/products/`;
   const options = {
      'method': 'GET',
      'headers' : {
         'Content-Type': 'application/json'
         ,'Authorization': `Bearer ${localStorage.getItem('access')}`
      }
   }
   
   try {
      const response = await fetch(productsEndPoint, options);
      if (response.ok) {
         const data = await response.json();
         console.log(data.results);
      }
   }catch(err) {
      console.error("err", err);
   }
}