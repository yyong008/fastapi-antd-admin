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

export const getDocsFeedbackById = async (id: number) => {
  try {
    const res = await request.get(`/api/admin/docs/feedback/${id}`);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const updateDocsFeedback = async (id: number, data: any) => {
  try {
    const res = await request.put(`/api/admin/docs/feedback/${id}`, data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const createDocsFeedback = async (data: any) => {
  try {
    const res = await request.post("/api/admin/docs/feedback/", data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const deleteDocsFeedbackByIds = async (ids: number[]) => {
  try {
    const res = await request.delete(`/api/admin/docs/feedback/`, {
      data: {
        ids
      }
    });
    return res;
  } catch (error) {
    console.error(error);
  }
}

