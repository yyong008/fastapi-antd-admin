import { useMemo } from "react";

export const useCategories = (categories) => {
  const categoriesOptions = useMemo(() => {
    return (
      categories?.map((c: any) => {
        return {
          label: c.name,
          value: c.id,
        };
      }) ?? []
    );
  }, [categories]);

  return categoriesOptions;
}
