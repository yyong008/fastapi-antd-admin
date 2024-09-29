import { useMemo } from "react";

export const useTags = (tags) => {
  const tagsOptions = useMemo(() => {
    return (
      tags?.map((c: any) => {
        return {
          label: c.name,
          value: c.id,
        };
      }) ?? []
    );
  }, [tags]);

  return tagsOptions;
};
