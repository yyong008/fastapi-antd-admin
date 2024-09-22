import "quill/dist/quill.snow.css";

import { useEffect, useRef } from "react";

import Quill from "quill";

export const Editor = ({ onChange, content, setContent }: any) => {
  const editorRef = useRef<any>(null);
  const quillRef = useRef<any>(null);

  // Initialize Quill Editor
  const init = () => {
    if (editorRef.current && !quillRef.current) {
      quillRef.current = new Quill(editorRef.current, {
        theme: "snow",
      });

      quillRef.current?.on("text-change", () => {
        const newContent = quillRef.current?.root.innerHTML;
        onChange?.(newContent);
        setContent(newContent);
      });
    }
  };

  useEffect(() => {
    init(); // Initialize the editor

    // Cleanup when unmounting the component
    return () => {
      quillRef.current?.off("text-change");
    };
  }, []);

  useEffect(() => {
    // Ensure content is set after initialization
    if (quillRef.current && content) {
      quillRef.current.root.innerHTML = content;
    }
  }, [content]); // Only re-run when content changes

  return <div ref={editorRef} />;
};

export const QuillEditor = ({ content, setContent }: any) => {
  return (
    <>
      <Editor content={content} setContent={setContent} />
    </>
  );
};
