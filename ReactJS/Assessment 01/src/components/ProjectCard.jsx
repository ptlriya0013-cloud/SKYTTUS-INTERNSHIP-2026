const ProjectCard = ({ title, description, tech }) => {
  return (
    <div className="project-card">
      <h3>{title}</h3>
      <p>{description}</p>
      <span>{tech}</span>
    </div>
  );
};

export default ProjectCard;



/*
const ProjectCard = ({ title, description }) => {
  return (
    <div className="project-card">
      <h3>{title}</h3>
      <p>{description}</p>
    </div>
  );
};

export default ProjectCard;
*/