import request from "@/utils/request";

type TNewsCategory = {
  page: number;
  pageSize: number;
};

export type TNewsCategoryData = {
  name: string;
  description: string;
};

export const getNewsCategory = async (searchParams: TNewsCategory) => {
  try {
    const res = await request.get("/api/admin/news/category/", {
      params: { page: searchParams.page, pageSize: searchParams.pageSize },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const createNewsCategory = async (data: TNewsCategoryData) => {
  try {
    const res = await request.post("/api/admin/news/category/", data);
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const updateNewsCategoryById = async (
  id: number,
  data: TNewsCategoryData
) => {
  try {
    const res = await request.put("/api/admin/news/category/" + id, data);
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const deleteNewsCategoryByIds = async (data: { ids: number[] }) => {
  try {
    const res = await request.delete("/api/admin/news/category/", {
      data: data,
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};
