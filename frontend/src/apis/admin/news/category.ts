import request from "@/utils/request";

type TNewsCategory = {
  page: number;
  pageSize: number;
}

export const getNewsCategory = async (searchParams : TNewsCategory) => {
  try {
    const res = await request.get("/api/admin/news/category/", {
      params: { page: searchParams.page, pageSize: searchParams.pageSize },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};
