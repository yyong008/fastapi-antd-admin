import { BlogItem } from '@/components/Client/Blog/blog-item';
import { createFileRoute } from '@tanstack/react-router'
import { getBlogList } from '@/apis/client/blog';

export const Route = createFileRoute('/_client/blog')({
  component: BlogRoute,
  loaderDeps: ({ search }: any) => ({
    page: search.page || 1,
    pageSize: search.pageSize || 10,
  }),
  async loader({ deps }) {
    const result: any = await getBlogList({
      page: deps.page,
      pageSize: deps.pageSize,
    });
    if (result && result.code === 0) {
      return result.data;
    }
  },
})

export function BlogRoute() {
  const _data = Route.useLoaderData();
  const blogs = _data.list;
  return (
    <div className="flex flex-col pt-[140px] px-[20px] w-[70vw] min-h-[80vh]">
      <div>
        {blogs?.map((n: any) => {
          return <BlogItem data={n} key={n.id} />;
        })}
      </div>
    </div>
  );
}
