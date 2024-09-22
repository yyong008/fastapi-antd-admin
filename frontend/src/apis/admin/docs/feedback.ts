import request from "@/utils/request";

type TFeedback = {
  page: number;
  pageSize: number;
};

export const getDocsFeedback = async (searchParams: TFeedback) => {
  try {
    const res = await request.get("/api/admin/docs/feedback/", {
      params: { page: searchParams.page, pageSize: searchParams.pageSize },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};
