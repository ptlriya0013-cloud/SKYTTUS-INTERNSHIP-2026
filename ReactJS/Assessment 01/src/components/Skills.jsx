const Skills = () => {
  const skills = [
    { name: "HTML", level: "Advanced" },
    { name: "CSS", level: "Advanced" },
    { name: "JavaScript", level: "Intermediate" },
    { name: "React", level: "Intermediate" },
    { name: "Git", level: "Beginner" },
    { name: "Python", level: "Beginner"}
  ];

  return (
    <section className="section" id="skills">
      <h2>Skills</h2>

      <div className="skill-grid">
        {skills.map((skill, index) => (
          <div className="skill-card" key={index}>
            <h3>{skill.name}</h3>
            <p>{skill.level}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Skills;








/*
const Skills = () => {
  const skills = ["HTML", "CSS", "JavaScript", "React", "Git"];

  return (
    <section id="skills" className="section">
      <h2>Skills</h2>
      <div className="skills">
        {skills.map((skill, index) => (
          <span key={index}>{skill}</span>
        ))}
      </div>
    </section>
  );
};

export default Skills;
*/