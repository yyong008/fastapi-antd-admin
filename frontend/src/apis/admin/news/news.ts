import request from "@/utils/request";

type TNewsCategory = {
  page: number;
  pageSize: number;
  category_id: number;
};

export const getNewsListByCategoryId = async (searchParams: TNewsCategory) => {
  try {
    const res = await request.get("/api/admin/news/", {
      params: {
        page: searchParams.page,
        pageSize: searchParams.pageSize,
        category_id: searchParams.category_id,
      },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const getNewsById = async (id: number) => {
  try {
    const res = await request.get("/api/admin/news/" + id);
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const createNews = async (data: any) => {
  try {
    const res = await request.post("/api/admin/news/", data);
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const updateNews = async (id, data: any) => {
  try {
    const res = await request.put("/api/admin/news/" + id, data);
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const deleteNewsByIds = async (data: { ids: number[] }) => {
  try {
    const res = await request.delete("/api/admin/news/", {
      data: data.ids,
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};
