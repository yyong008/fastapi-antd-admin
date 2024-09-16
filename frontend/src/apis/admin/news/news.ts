import request from "@/utils/request";

type TNewsCategory = {
  page: number;
  pageSize: number;
  category_id: number;
}

export const getNewsListByCategoryId = async (searchParams : TNewsCategory) => {
  try {
    const res = await request.get("/api/admin/news/", {
      params: { page: searchParams.page, pageSize: searchParams.pageSize, category_id: searchParams.category_id },
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
}
