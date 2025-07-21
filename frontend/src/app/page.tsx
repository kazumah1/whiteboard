'use client';
import { useRouter } from "next/navigation";
import "../common.scss";

export default function Page() {
  const router = useRouter();
  return (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100vh" }}>
      <h1 className="page-title">Welcome to OChem</h1>
      <button
        style={{ margin: "1rem", padding: "1rem 2rem", fontSize: "1.2rem" }}
        onClick={() => router.push("/load-lesson")}
      >
        Load Lesson
      </button>
      <button
        style={{ margin: "1rem", padding: "1rem 2rem", fontSize: "1.2rem" }}
        disabled
      >
        Generate Lesson (Coming Soon)
      </button>
    </div>
  );
}
