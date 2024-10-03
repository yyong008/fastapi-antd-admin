import { useEffect, useState } from "react";

import { ResponseStatus } from "@/constants/status";

export const useGetPageData = ({ request }) => {
  const [loading, setLoading] = useState(false);
  const [page, setPage] = useState({
    page: 1,
    pageSize: 10,
  });
  const [data, setData] = useState({
    list: [],
    total: 0,
  });

  const getData = async () => {
    const res: any = await request({ ...page });

    if (res && res.code === ResponseStatus.S) {
      setData(res.data);
      setLoading(false);
    }
  };

  useEffect(() => {
    setLoading(true);
    getData();
  }, [page]);

  return {
    data,
    setData,
    loading,
    page,
    setPage,
    getData
  }
}
