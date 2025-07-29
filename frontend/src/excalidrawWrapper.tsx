"use client";
import * as excalidrawLib from "@excalidraw/excalidraw";
import { Excalidraw } from "@excalidraw/excalidraw";

import "@excalidraw/excalidraw/index.css";

import App from "./components/ExampleApp";

const ExcalidrawWrapper: React.FC = () => {
  return (
    <>
      <App
        appTitle={"Lesson Title"}
        useCustom={(api: any, args?: any[]) => {}}
        excalidrawLib={excalidrawLib}
      >
        <Excalidraw />
      </App>
    </>
  );
};

export default ExcalidrawWrapper;
