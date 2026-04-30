export default function StudentCard({ name, age, email, city = "Unknown" }) {
  return (
    <div className="sma-student-card">
      <div className="sma-student-card-student"></div>
      <div className="sma-student-card-student-body">
        <h3 className="sma-student-card-stydent-name">{name}</h3>
        <p className="sma-student-card-student-detail">{email}</p>
        <div className="sma-student-card-student-footer">
          <span className="sma-student-card-student-age">Age {age}</span>
          <span className="sma-student-card-student-tag">{city}</span>
        </div>
      </div>
    </div>
  );
}
