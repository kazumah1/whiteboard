import dynamic from "next/dynamic";
import Script from "next/script";
import "../../common.scss";

export default function LoadLessonPage() {
  // Move dynamic import inside the component
  const ExcalidrawWithClientOnly = dynamic(
    () => import("../../excalidrawWrapper"),
    { ssr: false }
  );

  return (
    <>
      <a href="/">Back to Home</a>
      <h1 className="page-title">Load Lesson</h1>
      <Script id="load-env-variables" strategy="beforeInteractive">
        {`window["EXCALIDRAW_ASSET_PATH"] = window.origin;`}
      </Script>
      <ExcalidrawWithClientOnly />
    </>
  );
} 