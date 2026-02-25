import { useState } from "react";

const Contact = () => {
  const [formData, setFormData] = useState({
    name: "",
    mobile: "",
    email: "",
    message: "",
  });

  const [success, setSuccess] = useState(false);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
     alert("Your details will be saved ✅"); // 👈 popup alert
    setSuccess(true);

    // Clear form
    setFormData({
      name: "",
      mobile: "",
      email: "",
      message: "",
    });

    // Hide message after 3 seconds
    setTimeout(() => setSuccess(false), 3000);
  };

  return (
    <section id="contact" className="section contact-section">
      <h2>Contact Me</h2>

      <form className="contact-form" onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="Your Name"
          value={formData.name}
          onChange={handleChange}
          required
        />

        <input
          type="tel"
          name="mobile"
          placeholder="Mobile Number"
          value={formData.mobile}
          onChange={handleChange}
          required
        />

        <input
          type="email"
          name="email"
          placeholder="Email Address"
          value={formData.email}
          onChange={handleChange}
          required
        />

        <textarea
          name="message"
          placeholder="Your Message"
          value={formData.message}
          onChange={handleChange}
          required
        />

        <button type="submit">Save</button>








        {success && (
          <p className="success-msg">Your details will be saved ✅</p>
        )}
      </form>
    </section>
  );
};

export default Contact;




/*const Contact = () => {
  return (
    <section className="section" id="contact">
      <h2>Contact Me</h2>

      <form className="contact-form">
        <input type="text" placeholder="Your Name" />
        <input type="tel" placeholder="Mobile Number" />
        <input type="email" placeholder="Email Address" />
        <input type="text"  placeholder="Message"
        <button type="submit">Save</button>
      </form>
    </section>
  );
};

export default Contact;
*/





/*import { useState } from "react";

const Contact = () => {
  const [form, setForm] = useState({ name: "", email: "", message: "" });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!form.name || !form.email || !form.message) {
      alert("All fields are required");
      return;
    }

    alert("Message sent successfully!");
    setForm({ name: "", email: "", message: "" });
  };

  return (
    <section id="contact" className="section">
      <h2>Contact Me</h2>

      <form onSubmit={handleSubmit}>
        <input name="name" placeholder="Name" value={form.name} onChange={handleChange} />
        <input name="email" placeholder="Email" value={form.email} onChange={handleChange} />
        <textarea name="message" placeholder="Message" value={form.message} onChange={handleChange}></textarea>
        <button type="submit">Send</button>
      </form>
    </section>
  );
};

export default Contact;
*/