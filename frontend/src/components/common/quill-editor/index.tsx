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
    if (quillRef.current && content) {
      // Get current selection (cursor position)
      const range = quillRef.current.getSelection();

      // Use Quill's API to safely update the content
      if (quillRef.current.root.innerHTML !== content) {
        quillRef.current.clipboard.dangerouslyPasteHTML(content);
      }

      // Restore selection after content update
      if (range) {
        quillRef.current.setSelection(range.index, range.length);
      }
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
