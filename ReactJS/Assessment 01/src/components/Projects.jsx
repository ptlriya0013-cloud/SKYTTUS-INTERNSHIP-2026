import ProjectCard from "./ProjectCard";

const Projects = () => {
  return (
    <section className="section" id="projects">
      <h2>Projects</h2>

      <div className="projects">
        <ProjectCard
          title="CarbonWise 🌱"
          description="Climate Action platform aligned with SDG 13."
          tech="React • CSS • API"
        />
        <ProjectCard
          title="Personal Portfolio"
          description="Responsive portfolio using React & Vite."
          tech="React • Vite • Flexbox"
        />
         <ProjectCard
          title="Journey Junction"
          description="Find hidden gem for you."
          tech="React • Vite • Flexbox"
        />
        
      </div>
    </section>
  );
};

export default Projects;


/*
import ProjectCard from "./ProjectCard";

const Projects = () => {
  return (
    <section id="projects" className="section">
      <h2>Projects</h2>

      <div className="projects">
        <ProjectCard
          title="CarbonWise"
          description="Climate action project focused on SDG 13."
        />
        <ProjectCard
          title="Portfolio Website"
          description="Responsive portfolio built using ReactJS."
        />
      </div>
    </section>
  );
};

export default Projects;
*/